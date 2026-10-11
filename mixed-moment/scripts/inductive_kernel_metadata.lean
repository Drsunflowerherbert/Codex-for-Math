import MixedMoments
import Lean

/- Publication inspection only. The preserved complete-environment query
   already inspects every type and every definition/theorem/opaque value.
   This separate command also inspects inductive/constructor metadata and
   recursor reduction-rule right-hand sides. It creates no proof declarations. -/
open Lean Elab Command

run_cmd do
  let env ← getEnv
  let modules : Array Name := env.allImportedModuleNames.filter fun n =>
    n == `MixedMoments || (`MixedMoments).isPrefixOf n
  let helpers : Array Name := #[
    `MixedMoments.central._unsafe_rec, `MixedMoments.hStar._unsafe_rec,
    `MixedMoments.kminus._unsafe_rec, `MixedMoments.kplus._unsafe_rec,
    `MixedMoments.moment._unsafe_rec]
  let selected : Array (Name × ConstantInfo) :=
    (env.constants.toList.toArray.filter fun entry =>
      let projectOrigin := match env.getModuleIdxFor? entry.1 with
        | none => false
        | some idx => modules.contains env.allImportedModuleNames[idx.toNat]!
      let hasMetadata := match entry.2 with
        | .inductInfo _ | .ctorInfo _ | .recInfo _ => true
        | _ => false
      projectOrigin && hasMetadata).qsort fun a b => Name.lt a.1 b.1
  let expected : Array Name := #[
    `MixedMoments.MomentRecurrenceData,
    `MixedMoments.MomentRecurrenceData.mk,
    `MixedMoments.MomentRecurrenceData.rec]
  unless selected.size == expected.size && selected.all (fun row => expected.contains row.1) do
    throwError "Unexpected project inductive/constructor/recursor inventory"
  for (name, info) in selected do
    let (kind, metadataDependencies, rules) : String × Array Name × Array Json := match info with
      | .inductInfo v => ("inductive", (v.all ++ v.ctors).toArray, #[])
      | .ctorInfo v => ("constructor", #[v.induct], #[])
      | .recInfo v =>
        let ruleDependencies := v.rules.toArray.flatMap fun r => #[r.ctor] ++ r.rhs.getUsedConstants
        let ruleJson := v.rules.toArray.map fun r => Json.mkObj [
          ("constructor", Json.str r.ctor.toString),
          ("field_count", toJson r.nfields),
          ("rhs_expression", Json.str (reprStr r.rhs)),
          ("rhs_constant_dependencies", Json.arr (r.rhs.getUsedConstants.map fun n => Json.str n.toString))]
        ("recursor", v.all.toArray ++ ruleDependencies, ruleJson)
      | _ => ("unexpected", #[], #[])
    let allDependencies :=
      ((info.type.getUsedConstants ++ metadataDependencies).toList.eraseDups.toArray).qsort Name.lt
    let intersections := allDependencies.filter helpers.contains
    unless intersections.isEmpty do
      throwError "Compiler runtime helper occurs in kernel metadata for {name}"
    IO.println ("MM_METADATA_JSON " ++ (Json.mkObj [
      ("name", Json.str name.toString),
      ("kind", Json.str kind),
      ("type_expression", Json.str (reprStr info.type)),
      ("metadata_and_type_constant_dependencies", Json.arr (allDependencies.map fun n => Json.str n.toString)),
      ("recursor_rules", Json.arr rules),
      ("runtime_helper_intersections", Json.arr (intersections.map fun n => Json.str n.toString))]).compress)
  IO.println "MM_KERNEL_METADATA_COMPLETE"
