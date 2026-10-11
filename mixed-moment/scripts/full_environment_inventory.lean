import MixedMoments
import Lean

/- Audit query only: it creates no project proof declarations.  The module
   provenance map, rather than a namespace/name heuristic, selects constants. -/
open Lean Elab Command Meta

set_option pp.universes true
set_option pp.fullNames true
set_option pp.explicit true
set_option format.width 120
set_option maxHeartbeats 0

run_cmd do
  let env ← getEnv
  -- Python validates this passed report's source/config/checker hashes before
  -- executing the query and freezes the report itself through completion.
  let publicReport : Json ← Lean.ofExcept (Json.parse (← IO.FS.readFile "logs/certificates-lean-final-audit.json"))
  let publicStatusValue : Json ← Lean.ofExcept (publicReport.getObjVal? "status")
  let publicStatus : String ← Lean.ofExcept publicStatusValue.getStr?
  unless publicStatus == "passed" do throwError "Public audit is not passed"
  let publicResultsValue : Json ← Lean.ofExcept (publicReport.getObjVal? "axiom_results")
  let publicResults : Array Json ← Lean.ofExcept publicResultsValue.getArr?
  let reuseNames : Array String ← publicResults.mapM fun (row : Json) => do
    let declaration : Json ← Lean.ofExcept (row.getObjVal? "declaration")
    Lean.ofExcept declaration.getStr?
  let modules : Array Name := env.allImportedModuleNames.filter fun n =>
    n == `MixedMoments || (`MixedMoments).isPrefixOf n
  IO.println ("MM_MODULES_JSON " ++
    (Json.arr (modules.map fun n => Json.str n.toString)).compress)
  let constants : Array (Name × ConstantInfo) := (env.constants.toList.toArray.filter fun entry =>
    match env.getModuleIdxFor? entry.1 with
    | none => false
    | some idx => modules.contains env.allImportedModuleNames[idx.toNat]!).qsort fun a b => Name.lt a.1 b.1
  for (name, info) in constants do
    let some idx := env.getModuleIdxFor? name | continue
    let origin := env.allImportedModuleNames[idx.toNat]!
    unless modules.contains origin do continue
    let kind := match info with
      | .axiomInfo _ => "axiom"
      | .defnInfo _ => "definition"
      | .thmInfo _ => "theorem"
      | .opaqueInfo _ => "opaque"
      | .quotInfo _ => "quotient"
      | .inductInfo _ => "inductive"
      | .ctorInfo _ => "constructor"
      | .recInfo _ => "recursor"
    let (typeText, proposition) ← liftTermElabM do
      return ((← ppExpr info.type).pretty, ← isProp info.type)
    let valueDependencies := match info with
      | .defnInfo v => v.value.getUsedConstants
      | .thmInfo v => v.value.getUsedConstants
      | .opaqueInfo v => v.value.getUsedConstants
      | .inductInfo v => v.ctors.toArray
      | _ => #[]
    let dependencies := ((info.type.getUsedConstants ++ valueDependencies).toList.eraseDups.toArray).qsort Name.lt
    let runtimeParent := match name with
      | .str parent "_unsafe_rec" =>
        if Compiler.mkUnsafeRecName parent == name && env.isSafeDefinition parent then
          Json.str parent.toString
        else Json.null
      | _ => Json.null
    let record := Json.mkObj [
      ("name", Json.str name.toString),
      ("origin_module", Json.str origin.toString),
      ("kind", Json.str kind),
      ("universe_parameters", Json.arr (info.levelParams.toArray.map fun (n : Name) => Json.str n.toString)),
      ("type", Json.str typeText),
      ("type_expression", Json.str (reprStr info.type)),
      ("proposition_valued", Json.bool proposition),
      ("unsafe", Json.bool info.isUnsafe),
      ("partial", Json.bool info.isPartial),
      ("compiler_runtime_parent", runtimeParent),
      ("direct_kernel_dependencies", Json.arr (dependencies.map fun n => Json.str n.toString)),
      ("axiom_query_reused", Json.bool (reuseNames.contains name.toString))]
    IO.println ("MM_DECL_JSON " ++ record.compress)
    -- Invoke the ordinary command as well; identifiers are constructed from
    -- Names so private and numeric compiler-generated components are retained.
    unless reuseNames.contains name.toString do
      let id := mkIdent name
      elabCommand (← `(#print axioms $id))
  IO.println "MM_ENVIRONMENT_INVENTORY_COMPLETE"
