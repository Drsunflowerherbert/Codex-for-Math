import Lean
import Lean.Replay

/-!
Trusted live-evidence helper for Lean 4.24.0. Expected terms belong to a separately
reviewed harness, never imported theorem records. This version deliberately rejects
polymorphic target declarations. Replay uses the same Lean kernel implementation
against an imported dependency baseline; it is not an independent kernel checker.
-/

open Lean Elab Command Meta Term

namespace MathEvidence

private def kindOf (ci : ConstantInfo) : String :=
  match ci with
  | .thmInfo _ => "theorem"
  | .defnInfo _ => "definition"
  | .opaqueInfo _ => "opaque"
  | _ => "unsupported"

private def allowedAxiom (n : Name) : Bool :=
  n == `propext || n == `Classical.choice || n == `Quot.sound

private def validateTarget (ci : ConstantInfo) : CommandElabM Unit := do
  if ci.isUnsafe || ci.isPartial then
    throwError "unsafe or partial target is unsupported: {ci.name}"
  if kindOf ci == "unsupported" then
    throwError "unsupported declaration kind: {ci.name}"
  unless ci.levelParams.isEmpty do
    throwError "polymorphic target unsupported by this monomorphic contract: {ci.name}"
  if ci.type.hasMVar || ci.type.hasFVar || ci.type.hasLooseBVars then
    throwError "actual declaration type is not closed: {ci.name}"

elab "#evidence_check " n:ident " : " t:term : command => do
  let env ← getEnv
  -- Force completion of asynchronous kernel work. collectAxioms uses this same
  -- checked environment; the elaborator environment may contain preliminary data.
  let some ci := env.checked.get.find? n.getId
    | throwError "target missing from completed kernel environment: {n.getId}"
  validateTarget ci
  liftTermElabM do
    let expected ← elabType t
    synthesizeSyntheticMVarsNoPostponing
    let expected ← instantiateMVars expected
    if expected.hasMVar || expected.hasFVar || expected.hasLooseBVars then
      throwError "expected type is not closed: {n.getId}"
    unless ← withTransparency .all <| isDefEq ci.type expected do
      throwError "whole declaration type differs from expected type: {n.getId}"
    -- Check closed expressions with the kernel equality predicate as well. The
    -- full forall type is compared without instantiating implicit arguments.
    match Kernel.isDefEq env {} ci.type expected with
    | .ok true => pure ()
    | _ => throwError "kernel whole-type equality failed: {n.getId}"
    let axioms ← collectAxioms n.getId
    if axioms.any (!allowedAxiom ·) then
      throwError "unapproved axiom closure for {n.getId}: {axioms}"
    let record := Json.mkObj [
      ("target", Json.str n.getId.toString),
      ("declarationKind", Json.str <| kindOf ci),
      ("typeMatching", Json.str "closed_whole_type_kernel_definitional_equality"),
      ("axioms", Json.arr <| axioms.map fun a => Json.str a.toString),
      ("observedType", Json.str <| (← ppExpr ci.type).pretty),
      ("targetKernelReplay", Json.str "separate_phase_required")]
    logInfo m!"MATH_EVIDENCE_TARGET {record.compress}"

elab "#evidence_definition " n:ident " = " t:term : command => do
  let env ← getEnv
  let some ci := env.checked.get.find? n.getId
    | throwError "definition missing from completed kernel environment: {n.getId}"
  validateTarget ci
  let .defnInfo definition := ci
    | throwError "definition-body comparison requires a transparent definition: {n.getId}"
  if definition.value.hasMVar || definition.value.hasFVar || definition.value.hasLooseBVars then
    throwError "actual definition value is not closed: {n.getId}"
  liftTermElabM do
    let expected ← elabTerm t (some ci.type)
    synthesizeSyntheticMVarsNoPostponing
    let expected ← instantiateMVars expected
    if expected.hasMVar || expected.hasFVar || expected.hasLooseBVars then
      throwError "expected definition value is not closed: {n.getId}"
    unless ← withTransparency .all <| isDefEq definition.value expected do
      throwError "definition body differs from expected value: {n.getId}"
    match Kernel.isDefEq env {} definition.value expected with
    | .ok true => pure ()
    | _ => throwError "kernel definition-body equality failed: {n.getId}"
    let axioms ← collectAxioms n.getId
    if axioms.any (!allowedAxiom ·) then
      throwError "unapproved definition axiom closure for {n.getId}: {axioms}"
    let record := Json.mkObj [
      ("target", Json.str n.getId.toString),
      ("definitionBodyMatching", Json.str "kernel_definitional_equality"),
      ("axioms", Json.arr <| axioms.map fun a => Json.str a.toString),
      ("status", Json.str "definition_value_matched_not_a_proof_of_the_predicate")]
    logInfo m!"MATH_EVIDENCE_DEFINITION {record.compress}"

elab "#evidence_replay " "[" bases:ident,* "]" " targets "
    "[" targets:ident,* "]" : command => do
  let bases := bases.getElems.map Syntax.getId
  let targets := targets.getElems.map Syntax.getId
  if bases.isEmpty || targets.isEmpty then
    throwError "nonempty baseline modules and replay targets are required"
  let env ← getEnv
  -- Preserve proof bodies by inspecting the checked kernel environment. The
  -- regular env.constants map can export theorem bodies as axioms for modules.
  let baseline ← importModules (bases.map fun n => { module := n }) {}
  let mut newConstants : Std.HashMap Name ConstantInfo := {}
  for (name, ci) in env.checked.get.constants.toList do
    if !(baseline.find? name).isSome then
      if ci.isUnsafe || ci.isPartial then
        throwError "local replay closure contains unsafe/partial declaration: {name}"
      newConstants := newConstants.insert name ci
  for target in targets do
    let some ci := newConstants[target]?
      | throwError "replay target absent from local declaration closure: {target}"
    validateTarget ci
  let replayed ← baseline.replay newConstants
  for target in targets do
    unless (replayed.find? target).isSome do
      throwError "kernel replay did not retain target: {target}"
  let record := Json.mkObj [
    ("scope", Json.str "local_declaration_closure_same_kernel_imported_dependency_baseline"),
    ("baseModules", Json.arr <| bases.map fun a => Json.str a.toString),
    ("targets", Json.arr <| targets.map fun a => Json.str a.toString),
    ("replayedDeclarations", toJson newConstants.size),
    ("independentKernelReplay", Json.str "not_performed")]
  logInfo m!"MATH_EVIDENCE_REPLAY {record.compress}"

end MathEvidence
