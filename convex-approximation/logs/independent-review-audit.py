"""Independent frozen-source declaration/type/axiom audit; no implementation edits."""

from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re
import subprocess
import argparse


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path, default=Path("logs/current/independent"))
output = parser.parse_args().output
output.mkdir(parents=True, exist_ok=True)
sources = sorted(Path("ConvexApprox").glob("*.lean"))
root = Path("ConvexApprox.lean")
pins = [Path("lean-toolchain"), Path("lakefile.toml"), Path("lake-manifest.json")]
tracked = [root, *sources, *pins]


def source_hashes():
    return {str(p): sha256(p.read_bytes()).hexdigest() for p in tracked}


before = source_hashes()
module_names = {"ConvexApprox." + p.stem for p in sources}
imports = set(re.findall(r"^import\s+(\S+)", root.read_text(), re.MULTILINE))
assert module_names <= imports, "The root does not import every delivered module"
inventory = []
placeholder_findings = []
for path in sources:
    text = path.read_text()
    namespaces = re.findall(r"^namespace\s+(\S+)", text, re.MULTILINE)
    assert len(namespaces) == 1, f"Inspect namespace inventory manually: {path}"
    namespace = namespaces[0]
    for match in re.finditer(
        r"^(?:noncomputable\s+)?(theorem|lemma|def|structure|abbrev)\s+([^\s({:]+)",
        text,
        re.MULTILINE,
    ):
        kind, short_name = match.groups()
        inventory.append({"source": str(path), "kind": kind,
                          "name": namespace + "." + short_name})
    for match in re.finditer(r"\b(?:sorry|admit|sorryAx)\b|^\s*axiom\b", text, re.MULTILINE):
        placeholder_findings.append({"source": str(path), "token": match.group(),
                                     "line": text[:match.start()].count("\n") + 1})

assert len({row["name"] for row in inventory}) == len(inventory)
assert not placeholder_findings, placeholder_findings
audit_source = output / "independent-review-types-axioms.lean"
lines = ["import ConvexApprox", "set_option pp.universes true",
         "set_option pp.explicit true", ""]
for row in inventory:
    lines += ["#check @" + row["name"], "#print axioms " + row["name"]]
audit_source.write_text("\n".join(lines) + "\n")

argv = ["lake", "env", "lean", str(audit_source)]
started = datetime.now(timezone.utc).isoformat()
proc = subprocess.run(argv, text=True, capture_output=True)
audit_log = output / "independent-review-types-axioms.log"
audit_log.write_text("Independent exact declaration types and axiom dependencies\n"
                     + "UTC: " + started + "\n"
                     + "COMMAND: " + " ".join(argv) + "\n"
                     + proc.stdout + proc.stderr
                     + "EXIT STATUS: " + str(proc.returncode) + "\n")
after = source_hashes()
assert before == after, "The delivered source or pins changed during the audit"
allowed = {"propext", "Classical.choice", "Quot.sound"}
dependencies = []
for matched in re.finditer(r"depends on axioms:\s*\[([^\]]*)\]", proc.stdout):
    dependencies += [item.strip() for item in matched.group(1).split(",") if item.strip()]
unexpected = sorted(set(dependencies) - allowed)
record = {
    "started_utc": started,
    "command": argv,
    "exit_status": proc.returncode,
    "source_and_pin_sha256": before,
    "source_unchanged_during_audit": before == after,
    "module_count": len(sources),
    "declaration_count": len(inventory),
    "theorem_count": sum(row["kind"] in {"theorem", "lemma"} for row in inventory),
    "inventory": inventory,
    "placeholder_or_axiom_findings": placeholder_findings,
    "observed_axioms": sorted(set(dependencies)),
    "unexpected_axioms": unexpected,
}
(output / "independent-review-final-evidence.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({key: record[key] for key in ["exit_status", "module_count", "declaration_count",
                                             "theorem_count", "observed_axioms", "unexpected_axioms"]}, indent=2))
assert proc.returncode == 0, f"Read {audit_log}"
assert not unexpected, unexpected
