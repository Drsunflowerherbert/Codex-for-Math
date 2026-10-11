"""Inspected ZIP intake. Archive contents are bytes; no imported script executes."""
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import zipfile

CORPORA = {
    "supplement": {"file": "openai-math-reviewed-supplement-2026-10-11.zip", "bytes": 523782,
                   "sha256": "9e03b1ce33dc5d5fa62ab9478b06998bcb0eb32635fc11bccac065223e892a74"},
    "radial": {"file": "RadialContact-Reproducibility-v2-Lean4-4.24.0-2026-10-11.zip", "bytes": 167523,
               "sha256": "bdda223667986bb8e192c7e3f037ecfa430f2c37743441f240469dcc1de9b9d4"},
    "egyptian": {"file": "EgyptianExact-Lean4-4.24.0-2026-10-11.zip", "bytes": 297536,
                 "sha256": "22ebb1bbd0abdae7c8badfbf916c49aa39ad89f9d5f28b1dfa0e2e4530f33122"},
}
MAX_ARCHIVE = 32 * 1024 * 1024
MAX_EXPANDED = 32 * 1024 * 1024


def portable(name):
    return isinstance(name, str) and 0 < len(name) <= 240 and bool(re.fullmatch(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*", name)) and all(
        c not in (".", "..") and not c.endswith(".") and not re.match(r"^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)", c, re.I)
        for c in name.split("/"))


def safe_extract(archive, expected_hash, expected_bytes, output):
    if not re.fullmatch(r"[0-9a-f]{64}", expected_hash):
        raise ValueError("explicit expected archive SHA-256 required")
    archive = Path(archive)
    before = archive.lstat()
    if not stat.S_ISREG(before.st_mode) or before.st_size > MAX_ARCHIVE or before.st_size != expected_bytes:
        raise ValueError("archive type/size mismatch")
    fd = os.open(archive, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        opened = os.fstat(fd)
        if (opened.st_dev, opened.st_ino, opened.st_size) != (before.st_dev, before.st_ino, before.st_size):
            raise ValueError("archive identity changed before read")
        chunks, total = [], 0
        while True:
            b = os.read(fd, min(65536, expected_bytes + 1 - total))
            if not b:
                break
            total += len(b)
            if total > expected_bytes:
                raise ValueError("archive grew during read")
            chunks.append(b)
        raw = b"".join(chunks)
        after, linked = os.fstat(fd), archive.lstat()
        if (opened.st_dev, opened.st_ino, opened.st_size, opened.st_mtime_ns, opened.st_ctime_ns) != (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns, after.st_ctime_ns) or (linked.st_dev, linked.st_ino) != (opened.st_dev, opened.st_ino):
            raise ValueError("archive changed during read")
    finally:
        os.close(fd)
    if len(raw) != expected_bytes or hashlib.sha256(raw).hexdigest() != expected_hash:
        raise ValueError("archive does not match independent expected identity")
    import io
    staged, names, files, expanded = [], {}, set(), 0
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        infos = z.infolist()
        if len(infos) > 2000:
            raise ValueError("archive entry count limit")
        for info in infos:
            if info.orig_filename != info.filename or "\0" in info.orig_filename:
                raise ValueError("ZIP filename normalization or NUL truncation is unsupported")
            name = info.filename[:-1] if info.is_dir() else info.filename
            if not portable(name) or name.lower() in names:
                raise ValueError("unsafe, duplicate or case-colliding ZIP path")
            mode = info.external_attr >> 16
            if mode and stat.S_IFMT(mode) not in (0, stat.S_IFDIR if info.is_dir() else stat.S_IFREG):
                raise ValueError("ZIP links and special files are unsupported")
            if info.flag_bits & 1 or info.file_size > MAX_EXPANDED or expanded + info.file_size > MAX_EXPANDED:
                raise ValueError("encrypted or oversized ZIP entry")
            names[name.lower()] = name
            if not info.is_dir():
                data = z.read(info)  # CRC and decompression complete before writes.
                expanded += len(data)
                files.add(name.lower())
                staged.append((name, data))
        for name in names:
            parts = name.split("/")
            if any("/".join(parts[:i]) in files for i in range(1, len(parts))):
                raise ValueError("ZIP file/directory prefix collision")
    output = Path(os.path.abspath(output))
    parent = output.parent
    if parent.resolve() != parent:
        raise ValueError("extraction parent symlinks are rejected")
    if os.open not in os.supports_dir_fd or os.mkdir not in os.supports_dir_fd:
        raise ValueError("secure directory-relative extraction unsupported on this host")
    handles, directories, ancestors = [], {}, []
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_NONBLOCK
    try:
        pfd = os.open(parent.anchor, flags)
        handles.append(pfd)
        lexical = Path(parent.anchor)
        ancestors.append((lexical, os.fstat(pfd)))
        for component in parent.parts[1:]:
            pfd = os.open(component, flags, dir_fd=pfd)
            handles.append(pfd)
            lexical = lexical / component
            ancestors.append((lexical, os.fstat(pfd)))
        def stable_parents():
            for ancestor, observed in ancestors:
                linked = ancestor.lstat()
                if not stat.S_ISDIR(linked.st_mode) or (linked.st_dev, linked.st_ino) != (observed.st_dev, observed.st_ino):
                    raise ValueError("extraction parent ancestry changed")
        stable_parents()
        os.mkdir(output.name, dir_fd=pfd)
        root = os.open(output.name, flags, dir_fd=pfd)
        handles.append(root)
        directories[""] = (root, os.fstat(root))
        for name, data in staged:
            parts, current, key = name.split("/"), root, ""
            for component in parts[:-1]:
                key = key + "/" + component if key else component
                if key not in directories:
                    os.mkdir(component, dir_fd=current)
                    child = os.open(component, flags, dir_fd=current)
                    handles.append(child)
                    directories[key] = (child, os.fstat(child))
                current = directories[key][0]
            leaf = os.open(parts[-1], os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o666, dir_fd=current)
            try:
                with os.fdopen(leaf, "wb", closefd=False) as stream:
                    stream.write(data)
            finally:
                os.close(leaf)
        for key, (_, observed) in directories.items():
            linked = (output / key).lstat()
            if not stat.S_ISDIR(linked.st_mode) or (linked.st_dev, linked.st_ino) != (observed.st_dev, observed.st_ino):
                raise ValueError("extraction directory moved; no completed extraction")
        stable_parents()
    finally:
        for handle in reversed(handles):
            os.close(handle)
    return {"schema": "archive-intake-receipt/v1", "archive_bytes": expected_bytes, "archive_sha256": expected_hash,
            "files": [{"path": n, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()} for n, b in sorted(staged)],
            "expanded_bytes": expanded, "output": str(output), "executed_imported_contents": False,
            "lean_rerun": "not_performed_by_intake", "native_mrs": "unavailable_unvalidated"}


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in CORPORA:
        raise ValueError("Usage: python3 archive-intake.py supplement|radial|egyptian ARCHIVE NEW_DIRECTORY")
    identity = CORPORA[sys.argv[1]]
    receipt = safe_extract(sys.argv[2], identity["sha256"], identity["bytes"], sys.argv[3])
    receipt["archive_identity"] = identity
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(json.dumps({"ok": False, "message": str(error), "lean_pass": False}), file=sys.stderr)
        sys.exit(2)
