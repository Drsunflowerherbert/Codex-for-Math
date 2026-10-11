"use strict";
// Math exchange v1: imported data never executes commands; no Lean pass status exists.
function mathExchangeFactory(parseStrict) {
  "use strict";
  const SCHEMA = "math-exchange/v1";
  const LIMITS = Object.freeze({records: 2048, files: 1000, fileBytes: 16777216, totalBytes: 16777216, textChars: 2097152});
  const HEX40 = /^[0-9a-f]{40}$/;
  const HEX64 = /^[0-9a-f]{64}$/;
  const ID = /^[A-Za-z][A-Za-z0-9_.-]{0,127}$/;
  const NAME = /^[A-Za-z_][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_']*)*$/;
  const ROLES = ["source", "toolchain", "lockfile", "review", "experiment", "legacy_log", "statement_inventory"];
  const KINDS = ["definition", "theorem", "assumption"];
  const own = (o, k) => Object.prototype.hasOwnProperty.call(o, k);
  const plain = x => x !== null && typeof x === "object" && !Array.isArray(x) &&
    (Object.getPrototypeOf(x) === Object.prototype || Object.getPrototypeOf(x) === null);
  function encodeUTF8(s) {
    if (typeof s !== "string") throw new TypeError("UTF-8 input must be a string");
    const out = [];
    for (let i = 0; i < s.length; i++) {
      let n = s.charCodeAt(i);
      if (n >= 0xd800 && n <= 0xdbff) {
        const next = s.charCodeAt(++i);
        if (!(next >= 0xdc00 && next <= 0xdfff)) throw new TypeError("Unpaired high surrogate");
        n = 0x10000 + ((n - 0xd800) << 10) + next - 0xdc00;
      } else if (n >= 0xdc00 && n <= 0xdfff) throw new TypeError("Unpaired low surrogate");
      if (n < 0x80) out.push(n);
      else if (n < 0x800) out.push(0xc0 | (n >> 6), 0x80 | (n & 63));
      else if (n < 0x10000) out.push(0xe0 | (n >> 12), 0x80 | ((n >> 6) & 63), 0x80 | (n & 63));
      else out.push(0xf0 | (n >> 18), 0x80 | ((n >> 12) & 63), 0x80 | ((n >> 6) & 63), 0x80 | (n & 63));
    }
    return Uint8Array.from(out);
  }
  function decodeUTF8(bytes) {
    const out = [];
    for (let i = 0; i < bytes.length;) {
      const first = bytes[i++];
      let n, count, minimum;
      if (first < 0x80) { n = first; count = 0; minimum = 0; }
      else if (first >= 0xc2 && first <= 0xdf) { n = first & 31; count = 1; minimum = 0x80; }
      else if (first >= 0xe0 && first <= 0xef) { n = first & 15; count = 2; minimum = 0x800; }
      else if (first >= 0xf0 && first <= 0xf4) { n = first & 7; count = 3; minimum = 0x10000; }
      else throw new TypeError("Invalid UTF-8 leading byte");
      if (i + count > bytes.length) throw new TypeError("Truncated UTF-8");
      for (let j = 0; j < count; j++) {
        const b = bytes[i++];
        if ((b & 0xc0) !== 0x80) throw new TypeError("Invalid UTF-8 continuation byte");
        n = (n << 6) | (b & 63);
      }
      if (n < minimum || n > 0x10ffff || (n >= 0xd800 && n <= 0xdfff)) throw new TypeError("Invalid UTF-8 code point");
      out.push(String.fromCodePoint(n));
    }
    return out.join("");
  }
  function isPortablePath(s) {
    return typeof s === "string" && s.length > 0 && s.length <= 240 &&
      /^[A-Za-z0-9_.-]+(?:\/[A-Za-z0-9_.-]+)*$/.test(s) &&
      s.split("/").every(p => p !== "." && p !== ".." && !p.endsWith(".") &&
        !/^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)/i.test(p));
  }
  function isHTTPS(s) {
    return typeof s === "string" && s.length <= 4096 &&
      /^https:\/\/[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?(?::[0-9]{1,5})?(?:\/[^\s\\?#@]*)?$/.test(s);
  }
  function snapshotJSON(value) {
    let nodes = 0;
    const active = new WeakSet();
    function walk(v, depth) {
      if (++nodes > 1000000 || depth > 64) throw new TypeError("JSON structure exceeds limits");
      if (v === null || typeof v === "boolean") return;
      if (typeof v === "string") {
        if (v.length > LIMITS.textChars) throw new TypeError("JSON string exceeds limits");
        encodeUTF8(v);
        return;
      }
      if (typeof v === "number") {
        if (!Number.isFinite(v)) throw new TypeError("Nonfinite JSON number");
        return;
      }
      if (!(Array.isArray(v) || plain(v))) throw new TypeError("Expected plain JSON data");
      if (active.has(v)) throw new TypeError("Circular JSON object");
      if (Object.getOwnPropertySymbols(v).length) throw new TypeError("Symbol keys are not JSON data");
      active.add(v);
      const descriptors = Object.getOwnPropertyDescriptors(v);
      for (const key of Object.keys(descriptors)) {
        const d = descriptors[key];
        if (Array.isArray(v) && key === "length") continue;
        if (!own(d, "value") || !d.enumerable) throw new TypeError("Accessors or nonenumerable JSON properties");
        if (Array.isArray(v) && !/^(0|[1-9][0-9]*)$/.test(key)) throw new TypeError("Named array property");
        walk(d.value, depth + 1);
      }
      if (Array.isArray(v) && Object.keys(descriptors).length !== v.length + 1) throw new TypeError("Sparse JSON array");
      active.delete(v);
    }
    walk(value, 0);
    return JSON.parse(JSON.stringify(value));
  }
  function makeInventory(catalog) {
    const lines = [
      "Math exchange inventory",
      "Repository: " + catalog.project.repository,
      "Revision: " + catalog.project.revision,
      "Branch label: " + catalog.project.branch,
      "Lean toolchain: " + catalog.project.lean_toolchain,
      "Mathlib revision: " + catalog.project.mathlib_revision,
      "Manifest files: " + catalog.files.length,
      "Lean passes: 0 (this format accepts no pass status)",
      "Statement binding: verbatim excerpt and declaration-name heuristic only; no Lean type matching",
      ""
    ];
    for (const r of catalog.records.slice().sort((a, b) => a.id < b.id ? -1 : a.id > b.id ? 1 : 0)) {
      lines.push(r.id + " | " + r.kind + " | " + r.name +
        " | review=" + r.review.status + " | experiment reports=" + r.experiments.length +
        " | lean=" + r.lean.status);
      lines.push("  Explicit assumptions: " + (r.assumptions.join(", ") || "(none declared)"));
      lines.push("  Declared dependencies: " + (r.dependencies.join(", ") || "(none declared)"));
      lines.push("  Source: " + r.statement.source_path + " | statement sha256=" + r.statement.sha256);
    }
    return lines.join("\n") + "\n";
  }
  async function checkCatalog(input, readBytes, hashBytes) {
    const errors = [];
    const add = (code, path, message) => errors.push({code, path, message});
    let catalog;
    try { catalog = snapshotJSON(input); }
    catch (e) { add("invalid_json_data", "$", String(e.message)); return {ok: false, errors}; }
    function object(x, path, keys) {
      if (!plain(x)) { add("type", path, "Expected object"); return false; }
      for (const k of Object.keys(x)) if (!keys.includes(k)) add("unknown_field", path + "." + k, "Field is not supported");
      for (const k of keys) if (!own(x, k)) add("missing_field", path + "." + k, "Required field is absent");
      return true;
    }
    function string(x, path, pattern) {
      if (typeof x !== "string" || !x.length || x.length > LIMITS.textChars || /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/.test(x)) {
        add("type", path, "Expected nonempty Unicode string without forbidden control characters"); return false;
      }
      if (pattern && !pattern.test(x)) { add("format", path, "String has unsupported format"); return false; }
      return true;
    }
    function enumeration(x, path, choices) {
      if (!choices.includes(x)) { add("unsupported_value", path, "Expected one of " + choices.join(", ")); return false; }
      return true;
    }
    function array(x, path, max, min) {
      if (!Array.isArray(x) || x.length > max || x.length < (min || 0)) {
        add("type", path, "Expected array with length " + (min || 0) + ".." + max); return false;
      }
      return true;
    }
    function refs(x, path, max) {
      if (!array(x, path, max)) return;
      const seen = new Set();
      x.forEach((s, i) => {
        string(s, path + "[" + i + "]", ID);
        if (seen.has(s)) add("duplicate_reference", path + "[" + i + "]", "Duplicate record reference");
        seen.add(s);
      });
    }
    function evidence(x, path, statusRequiresEvidence) {
      if (!array(x, path, LIMITS.files, statusRequiresEvidence ? 1 : 0)) return;
      const seen = new Set();
      x.forEach((s, i) => {
        if (!isPortablePath(s)) add("unsafe_path", path + "[" + i + "]", "Expected portable relative file path");
        if (seen.has(s)) add("duplicate_evidence", path + "[" + i + "]", "Duplicate evidence path");
        seen.add(s);
      });
    }
    if (!object(catalog, "$", ["schema", "project", "files", "records"])) return {ok: false, errors};
    enumeration(catalog.schema, "$.schema", [SCHEMA]);
    if (object(catalog.project, "$.project", ["repository", "revision", "branch", "lean_toolchain", "mathlib_revision"])) {
      if (!isHTTPS(catalog.project.repository)) add("format", "$.project.repository", "Expected HTTPS repository URL without query, fragment, or credentials");
      string(catalog.project.revision, "$.project.revision", HEX40);
      if (!string(catalog.project.branch, "$.project.branch", /^[A-Za-z0-9][A-Za-z0-9_./-]{0,127}$/) ||
        (typeof catalog.project.branch === "string" && (catalog.project.branch.includes("..") || catalog.project.branch.endsWith("/"))))
        add("branch_label", "$.project.branch", "Expected conservative branch label");
      string(catalog.project.lean_toolchain, "$.project.lean_toolchain", /^leanprover\/lean4:v(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)$/);
      string(catalog.project.mathlib_revision, "$.project.mathlib_revision", HEX40);
    }
    const fileMap = new Map(), foldedPaths = new Set(), recordMap = new Map(), names = new Set();
    if (array(catalog.files, "$.files", LIMITS.files, 3)) catalog.files.forEach((f, i) => {
      const p = "$.files[" + i + "]";
      if (!object(f, p, ["path", "sha256", "role"])) return;
      if (!isPortablePath(f.path)) add("unsafe_path", p + ".path", "Expected portable relative file path");
      string(f.sha256, p + ".sha256", HEX64);
      enumeration(f.role, p + ".role", ROLES);
      if (fileMap.has(f.path) || (typeof f.path === "string" && foldedPaths.has(f.path.toLowerCase())))
        add("duplicate_file", p + ".path", "Duplicate or case-colliding file path");
      fileMap.set(f.path, f);
      if (typeof f.path === "string") foldedPaths.add(f.path.toLowerCase());
    });
    for (let i = 0; Array.isArray(catalog.files) && i < catalog.files.length; i++) {
      const path = catalog.files[i] && catalog.files[i].path;
      if (typeof path !== "string") continue;
      const segments = path.toLowerCase().split("/");
      for (let j = 1; j < segments.length; j++) {
        if (foldedPaths.has(segments.slice(0, j).join("/")))
          add("path_prefix_collision", "$.files[" + i + "].path", "A manifest file is also a case-folded parent directory of this file");
      }
    }
    if (array(catalog.records, "$.records", LIMITS.records, 1)) catalog.records.forEach((r, i) => {
      const p = "$.records[" + i + "]";
      if (!object(r, p, ["id", "kind", "name", "statement", "assumptions", "dependencies", "sources", "review", "experiments", "lean"])) return;
      string(r.id, p + ".id", ID);
      enumeration(r.kind, p + ".kind", KINDS);
      string(r.name, p + ".name", NAME);
      if (recordMap.has(r.id)) add("duplicate_id", p + ".id", "Duplicate record identifier");
      recordMap.set(r.id, r);
      if (names.has(r.name)) add("duplicate_name", p + ".name", "Duplicate Lean declaration name");
      names.add(r.name);
      if (object(r.statement, p + ".statement", ["text", "source_path", "source_excerpt", "sha256"])) {
        string(r.statement.text, p + ".statement.text");
        string(r.statement.source_excerpt, p + ".statement.source_excerpt");
        if (!isPortablePath(r.statement.source_path)) add("unsafe_path", p + ".statement.source_path", "Expected portable relative file path");
        string(r.statement.sha256, p + ".statement.sha256", HEX64);
        if (r.statement.text !== r.statement.source_excerpt)
          add("statement_excerpt_mismatch", p + ".statement.text", "Statement text must equal the exact declaration excerpt");
        if (typeof r.name === "string" && typeof r.statement.source_excerpt === "string") {
          const shortName = r.name.split(".").pop();
          const keywords = r.kind === "theorem" ? ["theorem", "lemma"] : ["def"];
          const matches = keywords.some(k => {
            const prefix = k + " " + shortName;
            return r.statement.source_excerpt.startsWith(prefix) &&
              /^[\s:({[]/.test(r.statement.source_excerpt.slice(prefix.length, prefix.length + 1));
          });
          if (!matches) add("declaration_heuristic", p + ".statement.source_excerpt", "Excerpt must begin with the kind and short declaration name; this is not a Lean parser");
        }
      }
      refs(r.assumptions, p + ".assumptions", LIMITS.records);
      refs(r.dependencies, p + ".dependencies", LIMITS.records);
      if (array(r.sources, p + ".sources", LIMITS.files, 1)) r.sources.forEach((s, j) => {
        const q = p + ".sources[" + j + "]";
        if (!object(s, q, ["url", "revision", "locator"])) return;
        if (!isHTTPS(s.url)) add("format", q + ".url", "Expected HTTPS source URL");
        string(s.revision, q + ".revision", HEX40);
        string(s.locator, q + ".locator");
      });
      if (object(r.review, p + ".review", ["status", "evidence"])) {
        enumeration(r.review.status, p + ".review.status", ["not_reviewed", "review_reported"]);
        evidence(r.review.evidence, p + ".review.evidence", r.review.status === "review_reported");
        if (r.review.status === "not_reviewed" && Array.isArray(r.review.evidence) && r.review.evidence.length)
          add("inconsistent_status", p + ".review.evidence", "Unreviewed status must have no review evidence");
      }
      if (array(r.experiments, p + ".experiments", LIMITS.files)) r.experiments.forEach((e, j) => {
        const q = p + ".experiments[" + j + "]";
        if (!object(e, q, ["claim", "scope", "evidence"])) return;
        string(e.claim, q + ".claim");
        string(e.scope, q + ".scope");
        evidence(e.evidence, q + ".evidence", true);
      });
      if (object(r.lean, p + ".lean", ["status", "evidence", "reason"])) {
        enumeration(r.lean.status, p + ".lean.status", ["not_run", "historical_report"]);
        string(r.lean.reason, p + ".lean.reason");
        evidence(r.lean.evidence, p + ".lean.evidence", r.lean.status === "historical_report");
        if (r.lean.status === "not_run" && Array.isArray(r.lean.evidence) && r.lean.evidence.length)
          add("inconsistent_status", p + ".lean.evidence", "Not-run status must have no historical Lean evidence");
      }
    });
    if (errors.length) return {ok: false, errors};
    const requireRole = (path, role, at) => {
      if (!fileMap.has(path)) add("missing_file_reference", at, "File is absent from manifest");
      else if (fileMap.get(path).role !== role) add("evidence_role", at, "Expected manifest role " + role);
    };
    const adjacency = new Map(), indegree = new Map();
    for (const id of recordMap.keys()) { adjacency.set(id, []); indegree.set(id, 0); }
    catalog.records.forEach((r, i) => {
      const p = "$.records[" + i + "]";
      requireRole(r.statement.source_path, "source", p + ".statement.source_path");
      for (const [field, list] of [["assumptions", r.assumptions], ["dependencies", r.dependencies]]) list.forEach((id, j) => {
        if (!recordMap.has(id)) add("dead_reference", p + "." + field + "[" + j + "]", "Referenced record does not exist");
        else if (field === "assumptions" && recordMap.get(id).kind !== "assumption")
          add("assumption_kind", p + "." + field + "[" + j + "]", "Assumptions must reference assumption records");
        else if (field === "dependencies" && r.kind === "theorem" && recordMap.get(id).kind === "assumption" && !r.assumptions.includes(id))
          add("undeclared_assumption", p + "." + field + "[" + j + "]", "Direct assumption dependency must also be explicitly declared");
      });
      for (const id of new Set(r.assumptions.concat(r.dependencies))) if (recordMap.has(id)) {
        adjacency.get(id).push(r.id);
        indegree.set(r.id, indegree.get(r.id) + 1);
      }
      r.review.evidence.forEach((f, j) => requireRole(f, "review", p + ".review.evidence[" + j + "]"));
      r.experiments.forEach((e, j) => e.evidence.forEach((f, k) => requireRole(f, "experiment", p + ".experiments[" + j + "].evidence[" + k + "]")));
      r.lean.evidence.forEach((f, j) => requireRole(f, "legacy_log", p + ".lean.evidence[" + j + "]"));
    });
    const ready = [...indegree.keys()].filter(id => indegree.get(id) === 0), topological = [];
    for (let i = 0; i < ready.length; i++) {
      const id = ready[i]; topological.push(id);
      for (const child of adjacency.get(id)) {
        indegree.set(child, indegree.get(child) - 1);
        if (indegree.get(child) === 0) ready.push(child);
      }
    }
    if (topological.length !== catalog.records.length) add("dependency_cycle", "$.records", "Declared assumptions and dependencies contain a cycle");
    const toolchains = catalog.files.filter(f => f.role === "toolchain"), lockfiles = catalog.files.filter(f => f.role === "lockfile");
    if (toolchains.length !== 1) add("toolchain_count", "$.files", "Exactly one toolchain file is required");
    if (lockfiles.length !== 1) add("lockfile_count", "$.files", "Exactly one Lake lockfile is required");
    if (errors.length) return {ok: false, errors};
    if (typeof readBytes !== "function" || typeof hashBytes !== "function") {
      add("adapter", "$", "readBytes and hashBytes must be injected functions");
      return {ok: false, errors};
    }
    const bytesMap = new Map(), decoded = new Map(); let totalBytes = 0;
    for (let i = 0; i < catalog.files.length; i++) {
      const f = catalog.files[i], p = "$.files[" + i + "]";
      let bytes;
      try {
        const supplied = await readBytes(f.path);
        if (!(supplied instanceof Uint8Array)) throw new TypeError("Reader must return Uint8Array");
        if (supplied.length > LIMITS.fileBytes || totalBytes + supplied.length > LIMITS.totalBytes) throw new TypeError("File bytes exceed limits");
        bytes = Uint8Array.from(supplied);
        totalBytes += bytes.length;
      } catch (e) { add("file_read", p + ".path", "Read failed: " + String(e.message || e)); continue; }
      let digest;
      try { digest = await hashBytes(Uint8Array.from(bytes)); }
      catch (e) { add("hash_adapter", p + ".sha256", "Hash failed: " + String(e.message || e)); continue; }
      if (typeof digest !== "string" || !HEX64.test(digest)) add("hash_adapter", p + ".sha256", "Hasher must return lowercase SHA-256");
      else if (digest !== f.sha256) add("file_hash_mismatch", p + ".sha256", "File bytes do not match manifest SHA-256");
      else {
        bytesMap.set(f.path, bytes);
        if (["source", "toolchain", "lockfile"].includes(f.role)) {
          try { decoded.set(f.path, decodeUTF8(bytes)); }
          catch (e) { add("invalid_utf8", p + ".path", String(e.message)); }
        }
        if (["review", "experiment", "legacy_log"].includes(f.role) && !bytes.length)
          add("empty_evidence", p + ".path", "Evidence file is empty");
      }
    }
    if (decoded.has(toolchains[0].path) && decoded.get(toolchains[0].path).trim() !== catalog.project.lean_toolchain)
      add("toolchain_drift", "$.project.lean_toolchain", "Pinned toolchain does not match hash-checked toolchain bytes");
    if (decoded.has(lockfiles[0].path)) {
      try {
        if (typeof parseStrict !== "function") throw new TypeError("Strict JSON parser adapter is required");
        const lock = parseStrict(decoded.get(lockfiles[0].path));
        if (!plain(lock) || !Array.isArray(lock.packages)) throw new TypeError("Expected Lake lockfile packages array");
        const mathlib = lock.packages.filter(p => plain(p) && p.name === "mathlib");
        if (mathlib.length !== 1 || mathlib[0].rev !== catalog.project.mathlib_revision ||
          mathlib[0].type !== "git" ||
          !["https://github.com/leanprover-community/mathlib4", "https://github.com/leanprover-community/mathlib4.git"].includes(mathlib[0].url))
          add("mathlib_drift", "$.project.mathlib_revision", "Pinned mathlib revision and official Git repository must match the unique hash-checked lockfile entry");
      } catch (e) { add("lockfile_parse", "$.files", "Cannot inspect Lake lockfile: " + String(e.message)); }
    }
    for (let i = 0; i < catalog.records.length; i++) {
      const r = catalog.records[i], p = "$.records[" + i + "].statement";
      try {
        const digest = await hashBytes(encodeUTF8(r.statement.text));
        if (typeof digest !== "string" || !HEX64.test(digest)) add("hash_adapter", p + ".sha256", "Hasher must return lowercase SHA-256");
        else if (digest !== r.statement.sha256) add("statement_hash_mismatch", p + ".sha256", "Exact statement text does not match SHA-256");
      } catch (e) { add("hash_adapter", p + ".sha256", "Statement hashing failed: " + String(e.message || e)); }
      if (decoded.has(r.statement.source_path)) {
        const source = decoded.get(r.statement.source_path), first = source.indexOf(r.statement.source_excerpt);
        if (first < 0) add("source_excerpt_missing", p + ".source_excerpt", "Verbatim declaration excerpt is absent from hash-checked source");
        else if (source.indexOf(r.statement.source_excerpt, first + 1) >= 0)
          add("source_excerpt_ambiguous", p + ".source_excerpt", "Declaration excerpt occurs more than once in hash-checked source");
      }
    }
    if (errors.length) return {ok: false, errors};
    const counts = {definitions: 0, theorems: 0, assumptions: 0, reviewReported: 0, experimentReports: 0, historicalLeanReports: 0, leanPasses: 0};
    for (const r of catalog.records) {
      counts[r.kind === "definition" ? "definitions" : r.kind === "theorem" ? "theorems" : "assumptions"]++;
      counts.reviewReported += r.review.status === "review_reported" ? 1 : 0;
      counts.experimentReports += r.experiments.length;
      counts.historicalLeanReports += r.lean.status === "historical_report" ? 1 : 0;
    }
    return {
      ok: true, errors: [], schema: SCHEMA, catalog,
      summary: {records: catalog.records.length, files: catalog.files.length, hashCheckedBytes: totalBytes, counts,
        topologicalOrder: topological, statementBinding: "textual_excerpt_only", leanTypeMatching: "not_performed",
        leanCompilation: "not_performed", leanAxiomAudit: "not_performed", independentKernelReplay: "not_performed",
        assumptionCompleteness: "not_established", dependencyCompleteness: "not_established", experimentScopeValidation: "not_established", sourceRevisionAttestation: "not_performed"},
      inventory: makeInventory(catalog)
    };
  }
  class MathExchangeValidationError extends Error {
    constructor(errors) {
      super("Math exchange validation failed (" + errors.length + " error" + (errors.length === 1 ? "" : "s") + ")");
      this.name = "MathExchangeValidationError";
      this.code = "VALIDATION_FAILED";
      this.errors = errors;
    }
  }
  async function validate(catalog, readBytes, hashBytes) {
    const result = await checkCatalog(catalog, readBytes, hashBytes);
    if (!result.ok) throw new MathExchangeValidationError(result.errors);
    return result;
  }
  return Object.freeze({SCHEMA, LIMITS, validate, encodeUTF8, decodeUTF8, isPortablePath, MathExchangeValidationError});
}
module.exports = mathExchangeFactory(require('./strict-json.cjs').parseStrict);
