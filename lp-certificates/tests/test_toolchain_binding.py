"""Publication repair: the selected executable must be the byte-audited member."""
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import bridge


class ExecutableBindingTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name) / "release"
        self.bin = self.root / "bin"
        self.bin.mkdir(parents=True)
        self.official = self.bin / "lean"
        self.official.write_bytes(b"reviewed executable fixture\n")
        self.members = {"bin/lean": (self.official.stat().st_size,
                                     bridge.file_hash(self.official))}
        self.pins = mock.patch.object(bridge, "RELEASE_MEMBERS", self.members)
        self.pins.start()
        self.addCleanup(self.pins.stop)

    def test_hash_and_return_the_same_exact_regular_executable(self):
        identity = bridge._toolchain(self.bin)
        self.assertEqual(identity["lean"], str(self.official))
        self.assertEqual(identity["members"]["bin/lean"]["sha256"],
                         bridge.file_hash(Path(identity["lean"])))

    def test_sibling_directory_substitution_rejected(self):
        alternate = self.root / "alternate"
        alternate.mkdir()
        (alternate / "lean").write_bytes(b"unverified sibling executable\n")
        with self.assertRaises(bridge.BridgeError):
            bridge._toolchain(alternate)

    def test_sibling_never_reaches_a_compiler_launch(self):
        alternate = self.root / "alternate"
        alternate.mkdir()
        (alternate / "lean").write_bytes(b"unverified sibling executable\n")
        raw = (bridge.ROOT / "examples/optimal_constant_no_rows.json").read_bytes()
        with mock.patch.object(bridge.Runner, "run") as launch:
            result = bridge.check_raw([raw], Path(self.directory.name) / "attempt", alternate)
        launch.assert_not_called()
        self.assertEqual(result["status"], "failed")
        self.assertNotEqual(result["inputs"][0]["status"], "lean_checked")

    def test_executable_symlink_rejected(self):
        real = self.root / "real-lean"
        self.official.rename(real)
        self.official.symlink_to(real)
        with self.assertRaises(bridge.BridgeError):
            bridge._toolchain(self.bin)

    def test_directory_ancestry_symlink_rejected(self):
        alias = Path(self.directory.name) / "alias"
        alias.symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(bridge.BridgeError):
            bridge._toolchain(alias / "bin")

    def test_nonregular_executable_rejected_before_read(self):
        self.official.unlink()
        os.mkfifo(self.official)
        with self.assertRaises(bridge.BridgeError):
            bridge._toolchain(self.bin)

    def test_postflight_rejects_changed_selected_bytes(self):
        bridge._toolchain(self.bin)
        self.official.write_bytes(b"changed executable fixture\n")
        with self.assertRaises(bridge.BridgeError):
            bridge._toolchain(self.bin)


if __name__ == "__main__":
    unittest.main()
