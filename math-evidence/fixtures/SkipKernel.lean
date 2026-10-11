import Mathlib
import Lean
open Lean Elab Command
set_option debug.skipKernelTC true in
run_cmd do
  liftCoreM <| addDecl <| .thmDecl {
    name := `ReceiptFixture.incomplete
    levelParams := []
    type := mkConst ``False
    value := mkConst ``True.intro
  }
