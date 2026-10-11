"""Deterministic source/evidence checkpoint ZIP, with an inspectable byte manifest.

No imported command or archive content is executed. Output must be outside the
source tree. This packages evidence reports, never authenticates their events.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import zipfile

MAX_TOTAL = 128 * 1024 * 1024
MAX_FILE = 32 * 1024 * 1024
EXCLUDED = {"__pycache__", ".DS_Store"}


def portable(name):
    return isinstance(name, str) and 0 < len(name) <= 240 and bool(re.fullmatch(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*", name)) and all(
        c not in (".", "..") and not c.endswith(".") and not re.match(r"^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)", c, re.I)
        for c in name.split("/"))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def collect(root):
    staged, folded, total = [], set(), 0
    for directory, dirs, files in os.walk(root, followlinks=False):
        for name in dirs + files:
            entry = Path(directory) / name
            if entry.is_symlink():
                raise ValueError("source tree symlink rejected: " + str(entry))
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDED)
        for name in sorted(files):
            if name in EXCLUDED or name.endswith(".pyc"):
                continue
            entry = Path(directory) / name
            relative = entry.relative_to(root).as_posix()
            before = entry.lstat()
            if not portable(relative) or relative.lower() in folded or not stat.S_ISREG(before.st_mode) or before.st_size > MAX_FILE:
                raise ValueError("unsafe, duplicate, special or oversized source entry")
            with entry.open("rb") as stream:
                data = stream.read(min(before.st_size, MAX_FILE) + 1)
                after = os.fstat(stream.fileno())
            linked = entry.lstat()
            identity = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns, s.st_ctime_ns)
            if len(data) != before.st_size or identity(before) != identity(after) or identity(before) != identity(linked):
                raise ValueError("source changed during checkpoint read")
            folded.add(relative.lower())
            total += len(data)
            if total > MAX_TOTAL:
                raise ValueError("checkpoint total byte limit")
            staged.append((relative, data))
    return sorted(staged)


def package(root, output):
    root, output = Path(root).resolve(), Path(output).absolute()
    if output.is_relative_to(root) or output.parent.resolve() != output.parent:
        raise ValueError("checkpoint output must be outside source tree in a canonical parent")
    staged = collect(root)
    manifest = {"schema": "math-evidence-checkpoint-manifest/v1", "root": "math-evidence",
                "selfExcluded": True, "algorithm": "SHA-256", "files": [
                    {"path": name, "bytes": len(data), "sha256": sha(data)} for name, data in staged],
                "sourceRevision": "d00a89dd9ce6c8ef782234d28c93e69cb712c947",
                "excludedGeneratedFiles": ["__pycache__", "*.pyc", ".DS_Store"],
                "receiptAuthority": "reported_snapshot_no_imported_Lean_pass"}
    staged.append(("release-manifest.json", (json.dumps(manifest, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()))
    if any(name == "release-manifest.json" for name, _ in staged[:-1]):
        raise ValueError("virtual manifest collides with source file")
    with output.open("xb") as stream:
        with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for name, data in sorted(staged):
                info = zipfile.ZipInfo("math-evidence/" + name, date_time=(2026, 10, 11, 0, 0, 0))
                info.create_system = 3
                info.external_attr = (stat.S_IFREG | 0o644) << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    if [(n, sha(b)) for n, b in collect(root)] != [(n, sha(b)) for n, b in staged if n != "release-manifest.json"]:
        raise ValueError("source changed during checkpoint; archive is not a completed checkpoint")
    data = output.read_bytes()
    return {"schema": "deterministic-checkpoint-result/v1", "file": str(output), "bytes": len(data),
            "sha256": sha(data), "files": len(staged), "expandedBytes": sum(len(b) for _, b in staged),
            "importedLeanPasses": 0}


def inspect(archive_path, expected_sha):
    archive_path = Path(archive_path)
    before = archive_path.lstat()
    if not stat.S_ISREG(before.st_mode) or before.st_size > MAX_TOTAL + 16 * 1024 * 1024:
        raise ValueError("checkpoint archive type/size limit")
    fd = os.open(archive_path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        with os.fdopen(fd, "rb", closefd=False) as stream:
            opened = os.fstat(fd)
            raw = stream.read(min(before.st_size, MAX_TOTAL + 16 * 1024 * 1024) + 1)
            after = os.fstat(fd)
        identity = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns, s.st_ctime_ns)
        if identity(before) != identity(opened) or identity(opened) != identity(after) or identity(after) != identity(archive_path.lstat()) or len(raw) != before.st_size:
            raise ValueError("checkpoint archive changed during read")
    finally:
        os.close(fd)
    if not re.fullmatch(r"[a-f0-9]{64}", expected_sha) or sha(raw) != expected_sha:
        raise ValueError("checkpoint independent archive digest mismatch")
    import io
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        infos, names = z.infolist(), set()
        if len(infos) > 10000:
            raise ValueError("checkpoint entry limit")
        data, total = {}, 0
        for item in infos:
            if item.orig_filename != item.filename or not item.filename.startswith("math-evidence/"):
                raise ValueError("checkpoint name normalization or root mismatch")
            name = item.filename.removeprefix("math-evidence/")
            if not portable(name) or name.lower() in names or not stat.S_ISREG(item.external_attr >> 16) or item.flag_bits & 1 or item.file_size > MAX_FILE:
                raise ValueError("invalid checkpoint entry")
            total += item.file_size
            if total > MAX_TOTAL:
                raise ValueError("checkpoint expanded size limit")
            names.add(name.lower())
            data[name] = z.read(item)
        for name in names:
            parts = name.split("/")
            if any("/".join(parts[:i]) in names for i in range(1, len(parts))):
                raise ValueError("checkpoint file/directory prefix collision")
        def unique(pairs):
            result = {}
            for k, v in pairs:
                if k in result:
                    raise ValueError("duplicate manifest JSON key")
                result[k] = v
            return result
        manifest = json.loads(data.pop("release-manifest.json").decode("utf8"), object_pairs_hook=unique)
        if set(manifest) != {"schema", "root", "selfExcluded", "algorithm", "files", "sourceRevision", "excludedGeneratedFiles", "receiptAuthority"} or manifest.get("schema") != "math-evidence-checkpoint-manifest/v1" or manifest.get("selfExcluded") is not True or manifest.get("root") != "math-evidence" or manifest.get("algorithm") != "SHA-256" or manifest.get("sourceRevision") != "d00a89dd9ce6c8ef782234d28c93e69cb712c947" or manifest.get("receiptAuthority") != "reported_snapshot_no_imported_Lean_pass" or manifest.get("excludedGeneratedFiles") != ["__pycache__", "*.pyc", ".DS_Store"] or not isinstance(manifest.get("files"), list):
            raise ValueError("checkpoint manifest mismatch")
        if len(manifest["files"]) != len(data):
            raise ValueError("checkpoint coverage mismatch")
        listed = set()
        for entry in manifest["files"]:
            if set(entry) != {"path", "bytes", "sha256"} or not portable(entry["path"]) or type(entry["bytes"]) is not int or entry["bytes"] < 0 or not isinstance(entry["sha256"], str) or not re.fullmatch(r"[a-f0-9]{64}", entry["sha256"]):
                raise ValueError("invalid checkpoint manifest file metadata")
            name = entry["path"]
            if name in listed or name not in data or len(data[name]) != entry["bytes"] or sha(data[name]) != entry["sha256"]:
                raise ValueError("checkpoint file integrity mismatch")
            listed.add(name)
    return {"ok": True, "kind": "checkpoint_byte_integrity_only", "files": len(infos), "bytes": len(raw),
            "sha256": expected_sha, "importedLeanPasses": 0, "extractedOrExecutedContents": False}


if __name__ == "__main__":
    try:
        if len(sys.argv) == 4 and sys.argv[1] == "pack":
            result = package(sys.argv[2], sys.argv[3])
        elif len(sys.argv) == 4 and sys.argv[1] == "inspect":
            result = inspect(sys.argv[2], sys.argv[3])
        else:
            raise ValueError("Usage: python3 package.py pack SOURCE_ROOT NEW_ARCHIVE.zip | inspect ARCHIVE.zip EXPECTED_SHA256")
        print(json.dumps(result, sort_keys=True, indent=2))
    except Exception as error:
        print(json.dumps({"ok": False, "message": str(error), "importedLeanPasses": 0}), file=sys.stderr)
        sys.exit(2)
