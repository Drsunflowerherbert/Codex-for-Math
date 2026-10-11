"""Compare installed compiler/kernel bytes with the inspected pinned release archive.

The archive is a .tar.zst, not extracted here. The expected digest is from the
published tangent installer at d00a89dd9ce6c8ef782234d28c93e69cb712c947.
No network authentication/signature claim is made by this local comparison.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tarfile

ARCHIVE_SHA = "b14f5e5159219dd1a1956c3b806813319f5e94ccd5bdfd56f54520609a5bb5ec"
NAMES = ("bin/lean", "lib/lean/libleanshared.so", "lib/lean/libleanshared_1.so",
         "lib/lean/libleanshared_2.so", "lib/lean/libInit_shared.so")


def digest(stream):
    h, size = hashlib.sha256(), 0
    while True:
        b = stream.read(65536)
        if not b:
            return h.hexdigest(), size
        h.update(b)
        size += len(b)


def audit(repository):
    base = Path(repository).resolve() / "tangent-limit/.cache/onboarding/lean-dist"
    archive = base / "lean-4.24.0-linux.tar.zst"
    with archive.open("rb") as f:
        observed, size = digest(f)
    if observed != ARCHIVE_SHA:
        raise ValueError("archive differs from inspected installer pin")
    process = subprocess.Popen(["/usr/bin/zstd", "-dc", str(archive)], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=False)
    records = {}
    try:
        with tarfile.open(fileobj=process.stdout, mode="r|") as tar:
            for member in tar:
                name = member.name.removeprefix("lean-4.24.0-linux/")
                if name not in NAMES:
                    continue
                if not member.isfile() or name in records or member.name != "lean-4.24.0-linux/" + name:
                    raise ValueError("invalid or duplicate release member")
                with tar.extractfile(member) as source:
                    archive_hash, archive_bytes = digest(source)
                installed = base / "lean-4.24.0-linux" / name
                with installed.open("rb") as source:
                    installed_hash, installed_bytes = digest(source)
                if (archive_hash, archive_bytes) != (installed_hash, installed_bytes):
                    raise ValueError("installed release member differs: " + name)
                records[name] = {"bytes": archive_bytes, "sha256": archive_hash,
                                 "installed": str(installed.resolve()), "comparison": "exact_bytes_match"}
        error = process.stderr.read().decode("utf8")
        if process.wait(timeout=60) != 0:
            raise ValueError("zstd decompression failed: " + error)
    finally:
        if process.poll() is None:
            process.kill()
            process.wait(timeout=10)
        process.stdout.close()
        process.stderr.close()
    if set(records) != set(NAMES):
        raise ValueError("required compiler/kernel members missing")
    return {"schema": "local-pinned-toolchain-byte-audit/v1", "archive": str(archive),
            "archiveBytes": size, "archiveSha256": observed, "pinSource": "published tangent installer at d00a89dd9ce6c8ef782234d28c93e69cb712c947",
            "compilerAndRuntime": records, "status": "all_selected_installed_members_match_pinned_archive",
            "networkAuthentication": "not_performed", "releaseSignatureAuthentication": "not_performed",
            "hostRuntimeLibraries": "trusted_host_not_authenticated_by_this_audit"}


if __name__ == "__main__":
    try:
        print(json.dumps(audit(sys.argv[1]), indent=2, sort_keys=True))
    except Exception as error:
        print(json.dumps({"ok": False, "message": str(error)}), file=sys.stderr)
        sys.exit(2)
