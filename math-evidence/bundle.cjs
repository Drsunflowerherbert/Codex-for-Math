"use strict";
const {validate} = require("./core.cjs");
const {canonicalJSON} = require("./strict-json.cjs");
const MAX_BYTES = 16 * 1024 * 1024;
const HEX = /^(?:[0-9a-f]{2})*$/;
function bytesToHex(bytes) { return Array.from(bytes, n => n.toString(16).padStart(2,"0")).join(""); }
function hexToBytes(text) {
  if (typeof text !== "string" || text.length > MAX_BYTES * 2 || !HEX.test(text)) throw new Error("invalid/oversized lowercase byte hex");
  return Uint8Array.from(text.match(/../g) || [], x => parseInt(x,16));
}
function keys(obj, expected, where) {
  if (!obj || typeof obj !== "object" || Array.isArray(obj) || Object.getPrototypeOf(obj) !== Object.prototype ||
      Object.keys(obj).sort().join("|") !== expected.slice().sort().join("|")) throw new Error("invalid fields: " + where);
}
async function makeBundle(catalog, readBytes, hashBytes) {
  const snapshot = new Map(); let total = 0;
  const capture = async path => {
    const input = await readBytes(path);
    if (!(input instanceof Uint8Array)) throw new Error("readBytes must return Uint8Array");
    const copy = Uint8Array.from(input); total += copy.length;
    if (copy.length > MAX_BYTES || total > MAX_BYTES) throw new Error("bundle byte limit");
    snapshot.set(path, copy); return copy;
  };
  const validated = await validate(catalog, capture, hashBytes);
  catalog = validated.catalog;
  const files = catalog.files.slice().sort((a,b)=>a.path < b.path ? -1 : a.path > b.path ? 1 : 0)
    .map(f=>({path:f.path, sha256:f.sha256, hex:bytesToHex(snapshot.get(f.path))}));
  return canonicalJSON({schema:"math-bundle/v1",catalog,files}) + "\n";
}
async function readBundle(bundle, hashBytes) {
  keys(bundle, ["schema","catalog","files"], "bundle");
  if (bundle.schema !== "math-bundle/v1" || !Array.isArray(bundle.files) || bundle.files.length > 1000) throw new Error("unsupported bundle");
  const files = new Map(); let total = 0;
  for (const file of bundle.files) {
    keys(file,["path","sha256","hex"],"bundle file");
    if (typeof file.path !== "string" || files.has(file.path)) throw new Error("duplicate/invalid bundled path");
    const bytes = hexToBytes(file.hex); total += bytes.length;
    if (total > MAX_BYTES) throw new Error("bundle byte limit");
    if (await hashBytes(bytes) !== file.sha256) throw new Error("bundled byte hash mismatch: " + file.path);
    files.set(file.path, bytes);
  }
  if (!bundle.catalog || !Array.isArray(bundle.catalog.files) ||
      bundle.catalog.files.length !== files.size ||
      bundle.files.some(f=>!bundle.catalog.files.some(c=>c.path===f.path && c.sha256===f.sha256))) throw new Error("bundle/file manifest disagreement");
  const summary = await validate(bundle.catalog, path => {
    if (!files.has(path)) throw new Error("missing bundle file: " + path);
    return Uint8Array.from(files.get(path));
  }, hashBytes);
  return {catalog:summary.catalog, files, summary};
}
module.exports = {makeBundle,readBundle,bytesToHex,hexToBytes};
