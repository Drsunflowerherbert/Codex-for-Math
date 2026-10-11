import TangentLimit

open Lean Elab Command

-- Private names contain a numeric component, so build identifier syntax from
-- the actual environment name rather than spelling that component as text.
run_cmd do
  for (name, _) in (← getEnv).constants.toList do
    let text := name.toString
    if text == "_private.TangentLimit.PoleSpacing.0.TangentLimit.one_le_abs_natCast_sub" ||
        text == "_private.TangentLimit.PoleSpacing.0.TangentLimit.blockDelta_le_abs_poleOffset_sub_of_index_lt" then
      elabCommand (← `(command| #check $(mkIdent name)))
      elabCommand (← `(command| #print axioms $(mkIdent name)))
