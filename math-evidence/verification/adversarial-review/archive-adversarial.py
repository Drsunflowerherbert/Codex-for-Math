"""Actual Python stdlib ZIP/filesystem adversarial intake audit; no imported code runs."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import stat
import tempfile
import time
import traceback
import zipfile

TOOLKIT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("reviewed_archive_intake", TOOLKIT / "archive-intake.py")
intake = importlib.util.module_from_spec(spec)
spec.loader.exec_module(intake)
BASE = Path(tempfile.gettempdir())
BASE.mkdir(parents=True, exist_ok=True)
WORK = Path(tempfile.mkdtemp(prefix="archive-review-", dir=BASE))
RESULTS = []
SEQ = 0


def next_path(label):
    global SEQ
    SEQ += 1
    return WORK / (str(SEQ) + "-" + label)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check(name, expected, fn, mode="actual_Python_stdlib_ZIP_filesystem"):
    try:
        observed = fn()
        RESULTS.append(dict(name=name, expected=expected, pass_=True, mode=mode, observed=observed))
    except Exception:
        RESULTS.append(dict(name=name, expected=expected, pass_=False, mode=mode, error=traceback.format_exc()))


def make_archive(entries, compression=zipfile.ZIP_STORED):
    target = next_path("input.zip")
    with zipfile.ZipFile(target, "w", compression=compression) as z:
        for name, data, mode in entries:
            info = zipfile.ZipInfo(name)
            info.compress_type = compression
            if mode is not None:
                info.create_system = 3
                info.external_attr = mode << 16
            z.writestr(info, data)
    return target


def extract(archive, rejected=True):
    raw = archive.read_bytes()
    out = next_path("output")
    error = None
    result = None
    try:
        result = intake.safe_extract(archive, digest(raw), len(raw), out)
    except Exception as e:
        error = str(e)
    if rejected:
        assert error, "unexpected archive acceptance: " + repr(result)
        assert not out.exists(), "invalid ZIP began output creation"
    else:
        assert not error, error
        assert result["executed_imported_contents"] is False
        assert result["lean_rerun"] == "not_performed_by_intake"
    return dict(error=error, result=result, output=str(out))


def main():
    before_source = digest((TOOLKIT / "archive-intake.py").read_bytes())
    original_names = [name for name,item in intake.CORPORA.items() if (TOOLKIT / "corpora/original" / item["file"]).is_file()] if os.environ.get("MATH_EVIDENCE_OPTIONAL_CORPORA") == "1" else []
    before_originals = {name: digest((TOOLKIT / "corpora/original" / intake.CORPORA[name]["file"]).read_bytes()) for name in original_names}
    for name in ["../escape", "/absolute", "a/../b", "a/./b", "a\\b", "a//b", "NUL.txt", "COM1", "trailing.", "a:b", "./x", "con/x"]:
        check("ZIP-path-" + name, "reject unsafe path before creation", lambda name=name: extract(make_archive([(name, b"marker", None)])))
    for names in [["a", "A"], ["a", "a/x"], ["A", "a/x"]]:
        check("ZIP-collision-" + "-".join(names), "reject collision before creation", lambda names=names: extract(make_archive([(n, b"marker", None) for n in names])))
    for kind, mode in [("symlink", stat.S_IFLNK | 0o777), ("FIFO", stat.S_IFIFO | 0o600), ("socket", stat.S_IFSOCK | 0o600), ("directory-mode-file", stat.S_IFDIR | 0o755)]:
        check("ZIP-special-" + kind, "reject special member type before creation", lambda mode=mode: extract(make_archive([("x", b"target", mode)])))
    check("ZIP-duplicate-name", "reject duplicates before creation", lambda: extract(make_archive([("x", b"one", None), ("x", b"two", None)])))
    check("ZIP-valid-inert-code", "exact payloads; no imported executable content", lambda: valid_inert())
    check("ZIP-CRC-tamper", "CRC failure before creation", lambda: crc_tamper())
    check("ZIP-NUL-filename", "reject original malformed member name without silent truncation", lambda: nul_filename())
    check("ZIP-output-parent-symlink", "reject parent alias before creation", lambda: parent_symlink())
    check("ZIP-existing-output", "refuse overwrite; marker remains", lambda: existing_output())
    check("ZIP-growing-input", "read at most original size plus one; reject growth", lambda: growing_input(), "actual_Python_filesystem_with_os_read_ordering_hook")
    for swap in ["root", "nested"]:
        check("ZIP-extraction-race-" + swap, "directory descriptors prevent redirected leaf writes; no completed extraction", lambda swap=swap: race(swap), "actual_Python_filesystem_with_os_open_ordering_hook")
    check("ZIP-extraction-race-parent-ancestor", "destination parent ancestry cannot redirect initial root creation", lambda: parent_race(), "actual_Python_filesystem_with_os_open_ordering_hook")
    for name in original_names:
        item = intake.CORPORA[name]
        check("immutable-pinned-corpus-" + name, "exact archive bytes and files consumed; no Lean rerun or script execution", lambda name=name, item=item: original_corpus(name, item))
    after_originals = {name: digest((TOOLKIT / "corpora/original" / intake.CORPORA[name]["file"]).read_bytes()) for name in original_names}
    assert before_originals == after_originals, "original corpus archive changed"
    after_source = digest((TOOLKIT / "archive-intake.py").read_bytes())
    report = dict(schema="independent-archive-intake-adversarial/v1", timeUTC=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), work=str(WORK), beforeSourceSHA256=before_source, afterSourceSHA256=after_source, sourceUnchangedDuringRun=before_source == after_source, originalsUnchanged=True, optionalOriginalArchiveChecks=len(original_names), originalSHA256=after_originals, total=len(RESULTS), passed=sum(r["pass_"] for r in RESULTS), failed=[r for r in RESULTS if not r["pass_"]], results=RESULTS, leanRerun="not_performed_by_this_suite", nativeMRS="not_tested")
    (Path(__file__).parent / "archive-report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("total", "passed", "failed", "sourceUnchangedDuringRun", "originalsUnchanged")}, indent=2))
    return 1 if report["failed"] else 0


def valid_inert():
    marker = next_path("must-not-execute")
    code = ("from pathlib import Path\nPath(" + repr(str(marker)) + ").write_text('bad')\n").encode()
    archive = make_archive([("source/code.py", code, stat.S_IFREG | 0o755), ("evidence.txt", "ℝ π ∀ n 😀\n".encode(), None), ("empty/", b"", stat.S_IFDIR | 0o755)])
    result = extract(archive, False)
    assert not marker.exists()
    out = Path(result["output"])
    assert (out / "source/code.py").read_bytes() == code
    assert (out / "evidence.txt").read_bytes() == "ℝ π ∀ n 😀\n".encode()
    return result


def crc_tamper():
    archive = make_archive([("x", b"DISTINCT_PAYLOAD", None)])
    raw = archive.read_bytes().replace(b"DISTINCT_PAYLOAD", b"CHANGED__PAYLOAD")
    archive.write_bytes(raw)
    return extract(archive)


def nul_filename():
    archive = make_archive([("safeAA", b"marker", None)])
    raw = archive.read_bytes().replace(b"safeAA", b"safe\x00X")
    archive.write_bytes(raw)
    return extract(archive)


def parent_symlink():
    archive = make_archive([("x", b"marker", None)])
    real, link = next_path("real-parent"), next_path("parent-link")
    real.mkdir()
    link.symlink_to(real, target_is_directory=True)
    raw = archive.read_bytes()
    error = None
    try:
        intake.safe_extract(archive, digest(raw), len(raw), link / "output")
    except Exception as e:
        error = str(e)
    assert error and not (real / "output").exists()
    return dict(error=error, outsideUntouched=True)


def existing_output():
    archive = make_archive([("x", b"marker", None)])
    out = next_path("existing")
    out.mkdir()
    (out / "marker").write_bytes(b"preserve")
    raw = archive.read_bytes()
    error = None
    try:
        intake.safe_extract(archive, digest(raw), len(raw), out)
    except Exception as e:
        error = str(e)
    assert error and (out / "marker").read_bytes() == b"preserve"
    return dict(error=error, markerPreserved=True)


def growing_input():
    archive = make_archive([("x", b"marker", None)])
    raw, original_read = archive.read_bytes(), os.read
    total, injected = 0, False
    def hooked(fd, limit):
        nonlocal total, injected
        if not injected:
            injected = True
            with archive.open("ab") as stream:
                stream.write(b"A" * 1048576)
        b = original_read(fd, limit)
        total += len(b)
        return b
    out, error = next_path("grown-output"), None
    os.read = hooked
    try:
        intake.safe_extract(archive, digest(raw), len(raw), out)
    except Exception as e:
        error = str(e)
    finally:
        os.read = original_read
    assert error and injected and total <= len(raw) + 1 and not out.exists()
    return dict(error=error, originalBytes=len(raw), readBytes=total, injected=injected)


def race(swap):
    archive = make_archive([("d/x.txt", b"marker", None)])
    raw, out, outside = archive.read_bytes(), next_path("race-output"), next_path("outside")
    outside.mkdir()
    original_open, injected, error = os.open, False, None
    # Keep the implementation's capability guard meaningful when interposing
    # syscall ordering: hooked open still calls the actual dir_fd-capable syscall.
    original_support = set(os.supports_dir_fd)
    def hooked(name, flags, *args, **kwargs):
        nonlocal injected
        if str(name) == "x.txt" and kwargs.get("dir_fd") is not None and not injected:
            injected = True
            target = out if swap == "root" else out / "d"
            target.rename(Path(str(target) + ".original"))
            target.symlink_to(outside, target_is_directory=True)
        return original_open(name, flags, *args, **kwargs)
    os.open = hooked
    os.supports_dir_fd.add(hooked)
    try:
        intake.safe_extract(archive, digest(raw), len(raw), out)
    except Exception as e:
        error = str(e)
    finally:
        os.open = original_open
        os.supports_dir_fd.clear()
        os.supports_dir_fd.update(original_support)
    assert injected and error and not (outside / "x.txt").exists()
    return dict(injected=injected, error=error, outsideWriteAbsent=True)


def original_corpus(name, item):
    archive = TOOLKIT / "corpora/original" / item["file"]
    raw = archive.read_bytes()
    assert len(raw) == item["bytes"] and digest(raw) == item["sha256"]
    out = next_path("original-" + name)
    receipt = intake.safe_extract(archive, item["sha256"], item["bytes"], out)
    for item in receipt["files"]:
        assert digest((out / item["path"]).read_bytes()) == item["sha256"]
    return dict(files=len(receipt["files"]), expandedBytes=receipt["expanded_bytes"], archiveSHA256=receipt["archive_sha256"], leanRerun=receipt["lean_rerun"], importedContentsExecuted=receipt["executed_imported_contents"])


def parent_race():
    archive = make_archive([("x.txt", b"outside marker", None)])
    raw, outer, outside = archive.read_bytes(), next_path("outer"), next_path("outside-parent")
    (outer / "selected").mkdir(parents=True)
    (outside / "selected").mkdir(parents=True)
    parent, out = outer / "selected", outer / "selected" / "output"
    original_open, original_support = os.open, set(os.supports_dir_fd)
    injected, error, result = False, None, None
    def hooked(name, flags, *args, **kwargs):
        nonlocal injected
        if not injected and ((Path(name) == parent and kwargs.get("dir_fd") is None) or
                             (str(name) == outer.name and kwargs.get("dir_fd") is not None)):
            injected = True
            outer.rename(Path(str(outer) + ".original"))
            outer.symlink_to(outside, target_is_directory=True)
        return original_open(name, flags, *args, **kwargs)
    os.open = hooked
    os.supports_dir_fd.add(hooked)
    try:
        result = intake.safe_extract(archive, digest(raw), len(raw), out)
    except Exception as e:
        error = str(e)
    finally:
        os.open = original_open
        os.supports_dir_fd.clear()
        os.supports_dir_fd.update(original_support)
    assert injected, "parent race hook did not run"
    assert not (outside / "selected/output/x.txt").exists(), "ZIP escaped selected original parent before descriptor anchor"
    assert error, repr(result)
    return dict(injected=injected, error=error, outsideWriteAbsent=True)


if __name__ == "__main__":
    raise SystemExit(main())
