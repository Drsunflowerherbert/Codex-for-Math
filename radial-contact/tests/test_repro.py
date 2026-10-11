"""Failure-oriented tests using the original real compiled audit as a fixture."""
import copy
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_evidence as checker
import verify as verifier


class ReproducibilityTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = pathlib.Path(self.temporary.name)
        for name in ["RadialContact.lean", "lean-toolchain", "lakefile.toml",
                     "lake-manifest.json", "README.md", "ASSUMPTIONS.md"]:
            shutil.copyfile(ROOT / name, self.root / name)
        for name in ["RadialContact", "scripts", "tests"]:
            shutil.copytree(ROOT / name, self.root / name, ignore=shutil.ignore_patterns("__pycache__"))
        evidence = self.root / "evidence"
        evidence.mkdir()
        found = checker.declarations(self.root)
        audit = (ROOT / "evidence/original/theorems-and-axioms.log").read_text()
        statements, axioms = checker.parse_audit(audit, found)
        (evidence / "theorems-and-axioms.log").write_text(audit)
        (evidence / "AxiomAudit.lean").write_text(checker.audit_source(found))
        (evidence / "assumptions.json").write_text(json.dumps(checker.assumptions(found, statements, axioms)))
        (evidence / "regression-tests.log").write_text("Ran 20 tests in 0.2s\n\nOK\n")
        (evidence / "toolchain-current.log").write_text("Lean (version 4.24.0, fixture)\n")
        (evidence / "final-build.log").write_text("Build completed successfully (fixture).\n")
        (evidence / "resolved-dependencies.json").write_text(json.dumps(checker.check_pins(self.root)))
        self.record = {"schema_version": 2, "status": "passed", "exit_code": 0,
                       "source_sha256": checker.inputs(self.root),
                       "evidence_sha256": {n: checker.sha256(self.root / n) for n in checker.EVIDENCE_FILES},
                       "records": [{"command": c, "exit_code": 0, "log": logfile}
                                   for c, logfile in zip(checker.COMMANDS, checker.COMMAND_LOGS)],
                       "declarations": list(found), "axioms": axioms}
        self.save()

    def save(self):
        (self.root / "evidence/validation.json").write_text(json.dumps(self.record))

    def rejects(self, code):
        with self.assertRaises(checker.EvidenceError) as caught:
            checker.check_evidence(self.root)
        self.assertEqual(caught.exception.code, code)

    def rehash(self, name):
        self.record["evidence_sha256"][name] = checker.sha256(self.root / name)
        self.save()

    def test_original_compiled_audit_and_complete_fixture_pass(self):
        result = checker.check_evidence(self.root)
        self.assertEqual(result["declarations"], 47)
        self.assertEqual(set(result["axioms_found"]), checker.ALLOWED_AXIOMS)

    def test_changed_proof_source_is_stale(self):
        path = self.root / "RadialContact/Basic.lean"
        path.write_text(path.read_text() + "\n-- source changed\n")
        self.rejects("source_drift")

    def test_added_source_file_is_stale(self):
        (self.root / "RadialContact/New.lean").write_text("namespace RadialContact\nend RadialContact\n")
        self.rejects("source_drift")

    def test_missing_source_is_not_silently_skipped(self):
        (self.root / "RadialContact/Basic.lean").unlink()
        self.rejects("missing_file")

    def test_verifier_policy_drift_is_stale(self):
        path = self.root / "scripts/check_evidence.py"
        path.write_text(path.read_text() + "\n# policy changed\n")
        self.rejects("source_drift")

    def test_missing_validation_fails(self):
        (self.root / "evidence/validation.json").unlink()
        self.rejects("missing_file")

    def test_malformed_validation_fails(self):
        (self.root / "evidence/validation.json").write_text("{broken")
        self.rejects("malformed_json")

    def test_nonobject_validation_has_clear_failure(self):
        (self.root / "evidence/validation.json").write_text("[]")
        self.rejects("evidence_schema")

    def test_failed_verification_is_not_a_success(self):
        self.record.update(status="failed", exit_code=1, failure="build failed")
        self.save()
        self.rejects("failed_verification")

    def test_missing_required_evidence_fails(self):
        for name in sorted(checker.EVIDENCE_FILES):
            with self.subTest(name=name):
                path = self.root / name
                original = path.read_bytes()
                path.unlink()
                self.rejects("missing_file")
                path.write_bytes(original)

    def test_modified_build_log_is_stale(self):
        (self.root / "evidence/final-build.log").write_text("different build\n")
        self.rejects("stale_evidence")

    def test_omitting_evidence_hash_entry_fails(self):
        del self.record["evidence_sha256"]["evidence/final-build.log"]
        self.save()
        self.rejects("evidence_coverage")

    def test_empty_audit_fails_even_if_hash_is_updated(self):
        name = "evidence/theorems-and-axioms.log"
        (self.root / name).write_text("")
        self.rehash(name)
        self.rejects("audit_coverage")

    def test_one_missing_axiom_record_fails_even_if_hash_is_updated(self):
        name = "evidence/theorems-and-axioms.log"
        text = (self.root / name).read_text()
        text = text.replace("'RadialContact.UnitSphere' depends on axioms: [propext, Classical.choice, Quot.sound]\n", "", 1)
        (self.root / name).write_text(text)
        self.rehash(name)
        self.rejects("missing_axiom_record")

    def test_missing_complete_declaration_record_fails(self):
        name = "evidence/theorems-and-axioms.log"
        lines = (self.root / name).read_text().splitlines()
        (self.root / name).write_text("\n".join(lines[2:]) + "\n")
        self.rehash(name)
        self.rejects("audit_coverage")

    def test_duplicate_record_fails(self):
        name = "evidence/theorems-and-axioms.log"
        text = (self.root / name).read_text()
        text += "\n".join(text.splitlines()[:2]) + "\n"
        (self.root / name).write_text(text)
        self.rehash(name)
        self.rejects("duplicate_statement")

    def test_unexpected_axiom_fails(self):
        name = "evidence/theorems-and-axioms.log"
        text = (self.root / name).read_text().replace("[propext, Classical.choice, Quot.sound]", "[sorryAx]", 1)
        (self.root / name).write_text(text)
        self.rehash(name)
        self.rejects("unexpected_axiom")

    def test_stale_assumptions_fail_even_if_hash_is_updated(self):
        name = "evidence/assumptions.json"
        (self.root / name).write_text("{}")
        self.rehash(name)
        self.rejects("stale_assumptions")

    def test_missing_command_record_fails(self):
        self.record["records"].pop()
        self.save()
        self.rejects("command_coverage")

    def test_nonzero_command_outcome_fails(self):
        self.record["records"][2]["exit_code"] = 1
        self.save()
        self.rejects("command_failed")

    def test_unrun_regression_suite_fails(self):
        name = "evidence/regression-tests.log"
        (self.root / name).write_text("Ran 0 tests in 0.0s\n\nOK\n")
        self.rehash(name)
        self.rejects("regression_coverage")

    def test_unpinned_dependency_fails(self):
        path = self.root / "lake-manifest.json"
        manifest = json.loads(path.read_text())
        manifest["packages"][0]["rev"] = "main"
        path.write_text(json.dumps(manifest))
        with self.assertRaises(checker.EvidenceError) as caught:
            checker.check_pins(self.root)
        self.assertEqual(caught.exception.code, "dependency_pin")

    def test_wrong_lake_requirement_cannot_hide_commit_in_comment(self):
        path = self.root / "lakefile.toml"
        text = path.read_text().replace('rev = "' + checker.MATHLIB_COMMIT + '"', 'rev = "main"')
        path.write_text(text + "\n# " + checker.MATHLIB_COMMIT + "\n")
        with self.assertRaises(checker.EvidenceError) as caught:
            checker.check_pins(self.root)
        self.assertEqual(caught.exception.code, "dependency_pin")

    def test_comments_and_strings_do_not_invent_declarations(self):
        path = self.root / "RadialContact/Basic.lean"
        original = checker.declarations(self.root)
        path.write_text('/- theorem fake : True := by sorry /- nested -/ -/\n' + path.read_text())
        self.assertEqual(checker.declarations(self.root), original)
        self.assertNotIn("sorry", checker.lean_code('"escaped \\" sorry"'))

    def test_unsupported_declaration_syntax_fails_closed(self):
        path = self.root / "RadialContact/Basic.lean"
        path.write_text(path.read_text() + "\nopaque hidden : Nat := 0\n")
        with self.assertRaises(checker.EvidenceError) as caught:
            checker.declarations(self.root)
        self.assertEqual(caught.exception.code, "unsupported_source")

    def test_failed_new_execution_replaces_prior_success(self):
        passed = subprocess.CompletedProcess([], 0)
        with mock.patch.object(verifier.subprocess, "run", side_effect=[passed, OSError("lake unavailable")]):
            self.assertEqual(verifier.verify(self.root), 1)
        record = json.loads((self.root / "evidence/validation.json").read_text())
        self.assertEqual(record["status"], "failed")
        self.assertEqual(record["records"][-1]["exit_code"], 127)
        self.rejects("failed_verification")

    def test_cli_failure_returns_nonzero_and_machine_readable_reason(self):
        (self.root / "evidence/validation.json").unlink()
        result = subprocess.run([sys.executable, str(ROOT / "scripts/check_evidence.py"), "--root", str(self.root)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)["error"], "missing_file")


if __name__ == "__main__":
    unittest.main()
