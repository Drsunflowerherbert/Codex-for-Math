"use strict";
const fs = require("node:fs");
const path = require("node:path");
const crypto = require("node:crypto");
const core = require("./core.cjs");
const strict = require("./strict-json.cjs");
const bundle = require("./bundle.cjs");
const pins = require("./tangent-pins.cjs");
const {sha256,utf8} = require("./test-hash.cjs");
async function main() {
  const corpusText=fs.readFileSync(path.join(__dirname,"samples/tangent.bundle.json"),"utf8");
  const corpus=strict.parseStrict(corpusText);
  const nativeHash=b=>crypto.createHash("sha256").update(b).digest("hex");
  const restored=await bundle.readBundle(corpus,nativeHash);
  for(const [name,bytes] of [["empty",utf8("")],["abc",utf8("abc")],["million-a",utf8("a".repeat(1000000))],...restored.files]) {
    if(sha256(bytes)!==nativeHash(bytes))throw new Error("test SHA/native SHA disagreement: "+name);
  }
  const synthetic=await require("./core-tests.cjs").runCoreTests(core,nativeHash,'Node.js');
  const acceptance=await require("./tests.cjs").runTests(corpus,'Node.js');
  const cliMock=await require("./cli-mock-tests.cjs").runCLIMockTests(fs.readFileSync(path.join(__dirname,"cli.cjs"),"utf8"),
    {core,strict,bundle,pins},corpusText,JSON.stringify(restored.catalog),[...restored.files],nativeHash,'Node.js_with_mock_adapters');
  const materializerMock=await require("./materialize-mock-tests.cjs").runMaterializeMockTests(fs.readFileSync(path.join(__dirname,"materialize.cjs"),"utf8"),core,strict,nativeHash,"Node.js_with_mock_adapters");
  if(synthetic.passed!==synthetic.total||acceptance.failed||cliMock.failed||materializerMock.failed)throw new Error("test suite failed");
  console.log(JSON.stringify({runtime:"Node.js",synthetic:{passed:synthetic.passed,total:synthetic.total},
    acceptance:{passed:acceptance.passed},mockCLI:{passed:cliMock.passed},materializerMock:{passed:materializerMock.passed},
    nativeHashParity:true,leanExecution:"not_performed",realFilesystemSafetyTests:"not_performed"},null,2));
}
main().catch(e=>{console.error(e.errors||e);process.exitCode=1;});
