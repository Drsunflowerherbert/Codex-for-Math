"""Reproduce the actual checkpoint ZIP/filesystem checks without Lean."""
import hashlib
import importlib.util
import json
from pathlib import Path
import stat
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("checkpoint_package", ROOT / "package.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
base = Path(tempfile.mkdtemp(prefix="math-package-tests-"))
source = base / "source"
source.mkdir()
(source / "source.lean").write_text("theorem correct : 1 + 1 = 2 := by decide\n")
(source / "notes.txt").write_text("∀ n : ℕ, π > 0\n")
(source / "evidence.bin").write_bytes(bytes(range(256)))
(source / "__pycache__").mkdir()
(source / "__pycache__/generated.pyc").write_bytes(b"ignored")
results = []


def check(name, action):
    try:
        action()
        results.append({"name": name, "status": "passed"})
    except Exception as error:
        results.append({"name": name, "status": "failed", "error": str(error)})


def require(condition):
    if not condition:
        raise AssertionError("required checkpoint property failed")


def reject(action):
    try:
        action()
    except Exception:
        return
    raise AssertionError("unexpected acceptance")


first = module.package(source, base / "a.zip")
second = module.package(source, base / "b.zip")
check("actual deterministic ZIP bytes", lambda: require((base / "a.zip").read_bytes() == (base / "b.zip").read_bytes()))
check("actual regular byte closure accepts integrity only", lambda: module.inspect(base / "a.zip", first["sha256"]))
check("whole archive identity drift rejects", lambda: reject(lambda: module.inspect(base / "a.zip", "0" * 64)))
check("existing output cannot be overwritten", lambda: reject(lambda: module.package(source, base / "a.zip")))
check("output within source tree rejects", lambda: reject(lambda: module.package(source, source / "inside.zip")))
check("generated cache omitted", lambda: require(first["files"] == 4))
(source / "alias").symlink_to(source / "notes.txt")
check("source symlinks reject", lambda: reject(lambda: module.package(source, base / "symlink.zip")))
(source / "alias").unlink()
(base / "link.zip").symlink_to(base / "a.zip")
check("archive symlinks reject", lambda: reject(lambda: module.inspect(base / "link.zip", first["sha256"])))
with zipfile.ZipFile(base / "a.zip") as archive:
    entries = {entry.filename: archive.read(entry) for entry in archive.infolist()}


def malformed(name, change):
    altered = dict(entries)
    change(altered)
    output = base / (name + ".zip")
    with zipfile.ZipFile(output, "w") as archive:
        for filename, data in altered.items():
            info = zipfile.ZipInfo(filename)
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, data)
    reject(lambda: module.inspect(output, hashlib.sha256(output.read_bytes()).hexdigest()))


manifest = "math-evidence/release-manifest.json"
cases = [
    ("coherent unsupported pass authority rejects", "status", lambda data: data.__setitem__(manifest, data[manifest].replace(b"reported_snapshot_no_imported_Lean_pass", b"Lean_pass"))),
    ("missing attachment rejects", "missing", lambda data: data.pop("math-evidence/evidence.bin")),
    ("tampered attachment rejects", "tamper", lambda data: data.__setitem__("math-evidence/evidence.bin", b"changed")),
    ("unexpected attachment rejects", "extra", lambda data: data.__setitem__("math-evidence/extra", b"x")),
    ("traversal filename rejects", "traversal", lambda data: data.__setitem__("math-evidence/../escape", b"x")),
    ("prefix collision rejects", "prefix", lambda data: data.__setitem__("math-evidence/notes.txt/child", b"x")),
    ("wrong archive root rejects", "root", lambda data: data.__setitem__("outside", b"x")),
    ("duplicate manifest JSON key rejects", "duplicate", lambda data: data.__setitem__(manifest, data[manifest].replace(b'"root":"math-evidence"', b'"root":"math-evidence","root":"math-evidence"'))),
]
for title, name, change in cases:
    check(title, lambda name=name, change=change: malformed(name, change))
report = {"schema": "actual-checkpoint-packaging-tests/v1", "mode": "actual_Python_stdlib_filesystem_ZIP", "temporary": str(base),
          "passed": sum(result["status"] == "passed" for result in results), "total": len(results), "fixtureArchive": first,
          "results": results, "importedLeanPasses": 0}
(ROOT / "verification/packaging-tests.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
if report["passed"] != report["total"]:
    raise SystemExit(1)
