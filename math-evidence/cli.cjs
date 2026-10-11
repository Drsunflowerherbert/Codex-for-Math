"use strict";
const fs = require("node:fs/promises");
const constants = require("node:fs").constants;
const path = require("node:path");
const crypto = require("node:crypto");
const core = require("./core.cjs");
const {parseStrict} = require("./strict-json.cjs");
const {makeBundle,readBundle} = require("./bundle.cjs");
const {acceptTangent} = require("./tangent-pins.cjs");
const {readBounded} = require("./bounded-io.cjs");
const hashBytes = bytes => crypto.createHash("sha256").update(bytes).digest("hex");
const MAX_JSON = 32 * 1024 * 1024;
function contained(root, target) {
  const relative = path.relative(root,target);
  return relative !== ".." && !relative.startsWith(".." + path.sep) && !path.isAbsolute(relative);
}
function sameFile(a,b) { return a.dev === b.dev && a.ino === b.ino; }
async function readRegular(filename, maxBytes, expected) {
  const before = await fs.lstat(filename);
  if (!before.isFile() || before.isSymbolicLink() || before.size > maxBytes ||
      (expected && !sameFile(before,expected))) throw new Error("not an unchanged regular bounded file: " + filename);
  const handle = await fs.open(filename, constants.O_RDONLY | (constants.O_NOFOLLOW || 0) | (constants.O_NONBLOCK || 0));
  try {
    const stat = await handle.stat();
    if (!stat.isFile() || stat.size > maxBytes || !sameFile(before,stat)) throw new Error("file identity changed before open: " + filename);
    const bytes = await readBounded(handle,Math.min(maxBytes,stat.size));
    const after = await handle.stat(), linked = await fs.lstat(filename);
    if (bytes.length > maxBytes || !linked.isFile() || !sameFile(before,linked) || !sameFile(stat,after) ||
        stat.size !== after.size || stat.mtimeMs !== after.mtimeMs || stat.ctimeMs !== after.ctimeMs)
      throw new Error("file changed during read: " + filename);
    return bytes;
  } finally { await handle.close(); }
}
async function readJSON(filename) {
  return parseStrict(core.decodeUTF8(await readRegular(filename,MAX_JSON)));
}
async function sourceReader(rootName) {
  const root = await fs.realpath(rootName);
  if (!(await fs.stat(root)).isDirectory()) throw new Error("source root is not a directory");
  return async portable => {
    if (!core.isPortablePath(portable)) throw new Error("unsafe source path");
    let current = root;
    const ancestors = [];
    for (const component of portable.split("/")) {
      current = path.join(current,component);
      const stat = await fs.lstat(current);
      if (stat.isSymbolicLink()) throw new Error("source symlinks are rejected");
      ancestors.push({path:current,stat});
    }
    const target = await fs.realpath(current);
    if (!contained(root,target)) throw new Error("source escapes selected root");
    const stable = async () => {
      for (const entry of ancestors) {
        const now = await fs.lstat(entry.path);
        if (now.isSymbolicLink() || !sameFile(entry.stat,now)) throw new Error("source path changed during read");
      }
    };
    await stable();
    const bytes = await readRegular(target,core.LIMITS.fileBytes,ancestors[ancestors.length-1].stat);
    await stable();
    return bytes;
  };
}
const usage = [
  "Usage:",
  "  node cli.cjs validate CATALOG.json SOURCE_ROOT",
  "  node cli.cjs inventory CATALOG.json SOURCE_ROOT",
  "  node cli.cjs bundle CATALOG.json SOURCE_ROOT NEW_OUTPUT.json",
  "  node cli.cjs inspect-bundle BUNDLE.json",
  "  node cli.cjs accept-tangent BUNDLE.json",
  "Imported records are data. No Lean or imported commands are executed."
].join("\n");
async function main(argv) {
  const [command,...args] = argv;
  if (["validate","inventory","bundle"].includes(command)) {
    if (args.length !== (command === "bundle" ? 3 : 2)) throw new Error(usage);
    const catalog = await readJSON(args[0]), reader = await sourceReader(args[1]);
    if (command === "bundle") {
      const bytes = await makeBundle(catalog,reader,hashBytes);
      await fs.writeFile(args[2],bytes,{encoding:"utf8",flag:"wx"});
      return {ok:true,kind:"source_evidence_bundle",sha256:hashBytes(Buffer.from(bytes,"utf8")),leanPass:false};
    }
    const result = await core.validate(catalog,reader,hashBytes);
    if (command === "inventory") return result.inventory;
    return {ok:true,summary:result.summary};
  }
  if (command === "inspect-bundle" || command === "accept-tangent") {
    if (args.length !== 1) throw new Error(usage);
    const result = await readBundle(await readJSON(args[0]),hashBytes);
    return {ok:true,summary:result.summary.summary,
      ...(command === "accept-tangent" ? {acceptance:await acceptTangent(result.catalog,p=>result.files.get(p),hashBytes)} : {})};
  }
  throw new Error(usage);
}
if (require.main === module) {
  main(process.argv.slice(2)).then(result=>{
    process.stdout.write(typeof result === "string" ? result : JSON.stringify(result,null,2)+"\n");
  }).catch(error=>{
    process.stderr.write(JSON.stringify({ok:false,message:error.message,errors:error.errors||[]},null,2)+"\n");
    process.exitCode = 2;
  });
}
module.exports = {main,contained,sourceReader,readRegular,readJSON};
