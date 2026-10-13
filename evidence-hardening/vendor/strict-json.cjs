"use strict";
// JSON with duplicate decoded-key rejection and bounded recursion.
function parseStrict(text, maxChars = 32 * 1024 * 1024) {
  if (typeof text !== "string" || text.length > maxChars) throw new Error("JSON size/type limit");
  let i = 0;
  const ws = () => { while (/[\x20\x09\x0a\x0d]/.test(text[i] || "#")) i++; };
  const fail = message => { throw new Error(message + " at character " + i); };
  function string() {
    if (text[i] !== '"') fail("expected string");
    const start = i++;
    let escaped = false;
    while (i < text.length) {
      const c = text[i++];
      if (!escaped && c === '"') {
        let value;
        try { value = JSON.parse(text.slice(start, i)); } catch { fail("invalid string"); }
        for (let n = 0; n < value.length; n++) {
          const u = value.charCodeAt(n);
          if (u >= 0xd800 && u <= 0xdbff) {
            const v = value.charCodeAt(++n);
            if (!(v >= 0xdc00 && v <= 0xdfff)) fail("unpaired surrogate");
          } else if (u >= 0xdc00 && u <= 0xdfff) fail("unpaired surrogate");
        }
        return value;
      }
      if (!escaped && c === "\\") escaped = true;
      else escaped = false;
    }
    fail("unterminated string");
  }
  function value(depth) {
    if (depth > 64) fail("JSON nesting limit");
    ws();
    const c = text[i];
    if (c === '"') return string();
    if (c === "{") {
      i++; ws();
      const out = {}, seen = new Set();
      if (text[i] === "}") { i++; return out; }
      while (true) {
        ws(); const key = string();
        if (seen.has(key)) fail("duplicate object key " + key);
        if (["__proto__", "constructor", "prototype"].includes(key)) fail("forbidden object key");
        seen.add(key); ws();
        if (text[i++] !== ":") fail("expected colon");
        out[key] = value(depth + 1); ws();
        const next = text[i++];
        if (next === "}") return out;
        if (next !== ",") fail("expected comma or object end");
      }
    }
    if (c === "[") {
      i++; ws(); const out = [];
      if (text[i] === "]") { i++; return out; }
      while (true) {
        if (out.length >= 10000) fail("array length limit");
        out.push(value(depth + 1)); ws();
        const next = text[i++];
        if (next === "]") return out;
        if (next !== ",") fail("expected comma or array end");
      }
    }
    for (const [token, result] of [["true",true],["false",false],["null",null]]) {
      if (text.slice(i, i + token.length) === token) { i += token.length; return result; }
    }
    const number = /^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?/.exec(text.slice(i));
    if (number) {
      i += number[0].length; const n = Number(number[0]);
      if (!Number.isFinite(n)) fail("nonfinite JSON number");
      return n;
    }
    fail("expected JSON value");
  }
  const out = value(0); ws();
  if (i !== text.length) fail("trailing JSON content");
  return out;
}
function canonicalJSON(value) {
  if (value === null) return "null";
  if (typeof value === "string" || typeof value === "boolean") return JSON.stringify(value);
  if (typeof value === "number" && Number.isFinite(value)) return JSON.stringify(value);
  if (Array.isArray(value)) return "[" + value.map(canonicalJSON).join(",") + "]";
  if (typeof value === "object" && Object.getPrototypeOf(value) === Object.prototype) {
    return "{" + Object.keys(value).sort().map(k => JSON.stringify(k) + ":" + canonicalJSON(value[k])).join(",") + "}";
  }
  throw new Error("canonical JSON requires plain finite JSON data");
}
module.exports = {parseStrict, canonicalJSON};
