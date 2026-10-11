"use strict";
const {canonicalJSON} = require("./strict-json.cjs");
const {validate} = require("./core.cjs");
const PIN = {
  "schema": "tangent-acceptance/v1",
  "project": {
    "repository": "https://github.com/Drsunflowerherbert/Codex-for-Math",
    "revision": "d00a89dd9ce6c8ef782234d28c93e69cb712c947",
    "branch": "codex/tangent-limit",
    "lean_toolchain": "leanprover/lean4:v4.24.0",
    "mathlib_revision": "f897ebcf72cd16f89ab4577d0c826cd14afaafc7"
  },
  "files": [
    {
      "path": "tangent-limit/README.md",
      "sha256": "5be38954d69d42c1a0fb6a109983574b728b88c361af32cc9cb0d48e627f295a",
      "role": "source"
    },
    {
      "path": "tangent-limit/TangentLimit.lean",
      "sha256": "98c74e84ab564605a18c9cb87fb6112f8b7bf999349dfba1f9e3ead868faac02",
      "role": "source"
    },
    {
      "path": "tangent-limit/TangentLimit/Diophantine.lean",
      "sha256": "74116a224783c4d91265c73f276eab0e280f5d047c3cb32260ee10a6204807bf",
      "role": "source"
    },
    {
      "path": "tangent-limit/TangentLimit/Hypothesis.lean",
      "sha256": "6f9fb3e7a25e2ba27fba29faf93e88add77a8c0aa3a8de59be72ae7b9ea2562a",
      "role": "source"
    },
    {
      "path": "tangent-limit/TangentLimit/Limit.lean",
      "sha256": "05ea71aef2541bdc9137c8dd110c3d11d8e2ffc5b851e931aeeef027fdfb0336",
      "role": "source"
    },
    {
      "path": "tangent-limit/TangentLimit/LimitComparison.lean",
      "sha256": "9250070b23a25f76ad620c8fee0b353ffc5b04b5823177e4bf6b92a28473813c",
      "role": "source"
    },
    {
      "path": "tangent-limit/TangentLimit/NearestPole.lean",
      "sha256": "b6321c174149a6e7f264d1d31b4813954dfba14900b9ab15c21c4701a3dc4cec",
      "role": "source"
    },
    {
      "path": "tangent-limit/TangentLimit/NonPole.lean",
      "sha256": "3ca47fd29a14a8e1299782ed729f96252a6768a84c67742bc075fb1273496710",
      "role": "source"
    },
    {
      "path": "tangent-limit/TangentLimit/Summability.lean",
      "sha256": "b6308da63a70ae2e7d45719afc2a5af71935061f8c9ec383740010a3613bf273",
      "role": "source"
    },
    {
      "path": "tangent-limit/TangentLimit/Trigonometry.lean",
      "sha256": "169ede182499acaf928a19eacb4605c32c0f71a52e17ae7edc0e26912eb40039",
      "role": "source"
    },
    {
      "path": "tangent-limit/docs/SOURCES.md",
      "sha256": "fd1e849579926531aac21e4f5743e1c8d6460740c1bc9ecbdde6a050f67473c7",
      "role": "source"
    },
    {
      "path": "tangent-limit/docs/independent-review.md",
      "sha256": "5026dedb437641910b1583a8d81121457ef1755e79e7558f461d0d0f8d07f2eb",
      "role": "review"
    },
    {
      "path": "tangent-limit/docs/mathematical-proof.md",
      "sha256": "f52aa95b1c5829f26d1c72c4aa244b6fde7e9491f61d01dd52b9ebffd67d93d1",
      "role": "source"
    },
    {
      "path": "tangent-limit/docs/theorem-statements.md",
      "sha256": "aeade1452a9747b370e4c9b67cdcdeba14a6fab9915f7716c18ffb869533ae34",
      "role": "statement_inventory"
    },
    {
      "path": "tangent-limit/docs/verification-summary.json",
      "sha256": "dbeb8a2389d6fb0f549e433f6484b013ded7a755de5888be0fcdb01917e09af6",
      "role": "legacy_log"
    },
    {
      "path": "tangent-limit/lake-manifest.json",
      "sha256": "8f871ddcf1917c176ac801f24bc66c975e4562d4d7aab8193c45ef7f31d5ad03",
      "role": "lockfile"
    },
    {
      "path": "tangent-limit/lakefile.toml",
      "sha256": "dbb3f4f563156a8062f93ceb0aa660a12b60650d2f47fb0de4f32308fb25e451",
      "role": "source"
    },
    {
      "path": "tangent-limit/lean-toolchain",
      "sha256": "42779d67b81608af8a12aa4328d2ab47ca201925b3b2bd68369587b5340bb434",
      "role": "toolchain"
    },
    {
      "path": "tangent-limit/logs/final-build.log",
      "sha256": "0a34f9325b605efffd2947f7345a15c0dcfb9ec5d86aedbeb512aebe3bf67524",
      "role": "legacy_log"
    },
    {
      "path": "tangent-limit/logs/final-theorem-inventory.log",
      "sha256": "b6e66b3382e58831c6972b116617ada1d308f9d1157399d6fa96f124ad96ad57",
      "role": "legacy_log"
    },
    {
      "path": "tangent-limit/logs/source-audit.log",
      "sha256": "77b40abe9cb9340a20700fcf5fa745f233c5afe8724ebda3a4e7574360b2763d",
      "role": "legacy_log"
    },
    {
      "path": "tangent-limit/scripts/TheoremInventory.lean",
      "sha256": "0a5e8810ccc28e617482e5cd9ca9bf72f69d98e4e50651bd09488450a1993fa9",
      "role": "source"
    },
    {
      "path": "tangent-limit/scripts/build.sh",
      "sha256": "fbb7dcd71745678a3f18875cd75139db615be6377c14658641db52dcd8a40b1b",
      "role": "source"
    },
    {
      "path": "tangent-limit/scripts/environment.sh",
      "sha256": "701d4155694efb2b3893f01b20f3a496224ffea91f6595b60dcc4392eaf4e373",
      "role": "source"
    },
    {
      "path": "tangent-limit/scripts/setup.sh",
      "sha256": "e2a8c6ce4c6af2fd7387be5a043694cc017b8af4bad6fe143b3f03f819bd5e9b",
      "role": "source"
    },
    {
      "path": "tangent-limit/scripts/verify.sh",
      "sha256": "d9d5890f76eda58e5451ff320f8315cd54ee491938ca9c7f4b61f6853b881fa1",
      "role": "source"
    }
  ],
  "records": [
    {
      "id": "TangentLimit.PiDiophantine",
      "kind": "assumption",
      "source_path": "tangent-limit/TangentLimit/Hypothesis.lean",
      "sha256": "019661f0b94d661a9f84a9a54b3e270bfed25c0bedb41b043a84c6ff8a7d2ea2",
      "assumptions": [],
      "dependencies": []
    },
    {
      "id": "TangentLimit.abs_cos_eq_abs_sin_offset",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Trigonometry.lean",
      "sha256": "f098aec24abb330cf83fc1b1887c4bf375a158d74c4437dadc91525942946ac8",
      "assumptions": [],
      "dependencies": []
    },
    {
      "id": "TangentLimit.abs_poleOffset_le",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/NearestPole.lean",
      "sha256": "632a88abef2072a271698a526f66c4d693c32fca2fae051679c7eb3ac1071fcb",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.lt_poleIndex_add_one_mul_pi",
        "TangentLimit.poleDenom",
        "TangentLimit.poleIndex_mul_pi_le",
        "TangentLimit.poleOffset"
      ]
    },
    {
      "id": "TangentLimit.abs_tan_div_cube_eq",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Summability.lean",
      "sha256": "0e25f2c580016fc65aa57f36b87e218a00b14eb41e6a652f59faf5af09c716d9",
      "assumptions": [],
      "dependencies": []
    },
    {
      "id": "TangentLimit.chord_cos_bound",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Trigonometry.lean",
      "sha256": "a3778c8dfd411dda04f8e478d69f2dced4e98c1285c3f8dd4179796009476fac",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.abs_cos_eq_abs_sin_offset"
      ]
    },
    {
      "id": "TangentLimit.cos_intCast_ne_zero",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/NonPole.lean",
      "sha256": "f42ee038a1190f3c4f2e9ce5c2aa338282fe708f4e0a5472158f773f795b6b09",
      "assumptions": [],
      "dependencies": []
    },
    {
      "id": "TangentLimit.cos_natCast_ne_zero",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/NonPole.lean",
      "sha256": "8222929c2475bd8d98b5821034940153a0c8bfd30b2292258d85470690ba8403",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.cos_intCast_ne_zero"
      ]
    },
    {
      "id": "TangentLimit.eventual_abs_tan_div_cube_le_rpow",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Summability.lean",
      "sha256": "497bb56607d0d035109a70b4b7fa3b68ae4b39aa83aef15c4b34f52c7d437190",
      "assumptions": [
        "TangentLimit.PiDiophantine"
      ],
      "dependencies": [
        "TangentLimit.eventually_tan_le_pole_rpow",
        "TangentLimit.poleDenom",
        "TangentLimit.poleDenom_le_two_mul"
      ]
    },
    {
      "id": "TangentLimit.eventually_abs_tan_le_quadratic",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Limit.lean",
      "sha256": "7371495f2d56903080c102becc7529215090a00c1cddc1001f90670d74271995",
      "assumptions": [
        "TangentLimit.PiDiophantine"
      ],
      "dependencies": [
        "TangentLimit.eventually_tan_le_pole_rpow",
        "TangentLimit.poleDenom",
        "TangentLimit.poleDenom_le_two_mul"
      ]
    },
    {
      "id": "TangentLimit.eventually_poleDenom_ge",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/NearestPole.lean",
      "sha256": "dbc9c7d401a21ce12a31108c7d74149dd5febf9ed952c283cf3aa05ba0bf8ce9",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.lt_poleIndex_add_one_mul_pi",
        "TangentLimit.poleDenom",
        "TangentLimit.poleIndex"
      ]
    },
    {
      "id": "TangentLimit.eventually_tan_le_pole_rpow",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Diophantine.lean",
      "sha256": "bb4d7e8c0151307e51dbd95440d70d29c1b6ef4971f7d963f478758a257e8c47",
      "assumptions": [
        "TangentLimit.PiDiophantine"
      ],
      "dependencies": [
        "TangentLimit.abs_poleOffset_le",
        "TangentLimit.eventually_poleDenom_ge",
        "TangentLimit.poleDenom",
        "TangentLimit.poleDenom_pos",
        "TangentLimit.poleIndex",
        "TangentLimit.tan_le_pole_power"
      ]
    },
    {
      "id": "TangentLimit.lt_poleIndex_add_one_mul_pi",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/NearestPole.lean",
      "sha256": "4fe3e5e713fd05bdd61822acdfb8b4a16900eb858e182bf43f53c497db836263",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.poleIndex"
      ]
    },
    {
      "id": "TangentLimit.poleDenom",
      "kind": "definition",
      "source_path": "tangent-limit/TangentLimit/NearestPole.lean",
      "sha256": "a3201328bf4ff01096660d7780b61a8ea94edf96547273056e357ffd0ee4991e",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.poleIndex"
      ]
    },
    {
      "id": "TangentLimit.poleDenom_le_two_mul",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/NearestPole.lean",
      "sha256": "2e9b831e7fdc4e28bf94fdcc1ae87978efb7a4b62001d8e10e38c6091c9eeb6c",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.poleDenom",
        "TangentLimit.poleIndex",
        "TangentLimit.poleIndex_mul_pi_le"
      ]
    },
    {
      "id": "TangentLimit.poleDenom_odd",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/NearestPole.lean",
      "sha256": "b20fda5ce9308d92abff7759bf0ae439456ed72175c9b24336c9efe998d3dd01",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.poleDenom",
        "TangentLimit.poleIndex"
      ]
    },
    {
      "id": "TangentLimit.poleDenom_pos",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/NearestPole.lean",
      "sha256": "cc1aee38919c45a6f4513bfc7dd417a1c5a26ff36d6995772ead3ee8a40e2f1c",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.poleDenom"
      ]
    },
    {
      "id": "TangentLimit.poleIndex",
      "kind": "definition",
      "source_path": "tangent-limit/TangentLimit/NearestPole.lean",
      "sha256": "86cc26b70845e34620c3bbb6be399368ca85332738973da9bd7ccb31c5be598b",
      "assumptions": [],
      "dependencies": []
    },
    {
      "id": "TangentLimit.poleIndex_mul_pi_le",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/NearestPole.lean",
      "sha256": "9e111ccc64c6e9d8f3c7797f8336e48a3e3343f8db0502349436a8bd177b32ff",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.poleIndex"
      ]
    },
    {
      "id": "TangentLimit.poleOffset",
      "kind": "definition",
      "source_path": "tangent-limit/TangentLimit/NearestPole.lean",
      "sha256": "d04f005fb901e73f3c12940aae3d50e4014f97b8081e2d58d0f645ee300b70a5",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.poleDenom"
      ]
    },
    {
      "id": "TangentLimit.poleOffset_nearest",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/NearestPole.lean",
      "sha256": "40f70e35a6f0a47da26bf3fcc5774f738a143f19165da6798d4fb8d20ce46d0b",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.abs_poleOffset_le",
        "TangentLimit.lt_poleIndex_add_one_mul_pi",
        "TangentLimit.poleDenom",
        "TangentLimit.poleIndex",
        "TangentLimit.poleIndex_mul_pi_le",
        "TangentLimit.poleOffset"
      ]
    },
    {
      "id": "TangentLimit.pole_distance_identity",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Diophantine.lean",
      "sha256": "da46e9602ac0b76d37b6ccd2c573e0516d4edb182c94b704e78b6079c93e40e2",
      "assumptions": [],
      "dependencies": []
    },
    {
      "id": "TangentLimit.pole_distance_lower_bound",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Diophantine.lean",
      "sha256": "1d344319f4a2639cf7f200a7da20653512ff5c53e6cae61c26364d399c3a102e",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.pole_distance_identity"
      ]
    },
    {
      "id": "TangentLimit.pole_distance_lower_bound_of_piDiophantine",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Diophantine.lean",
      "sha256": "cdfba30746e6f63e48641b6ff43e306e0d46606175062b76236957c995b5131f",
      "assumptions": [
        "TangentLimit.PiDiophantine"
      ],
      "dependencies": [
        "TangentLimit.pole_distance_lower_bound"
      ]
    },
    {
      "id": "TangentLimit.reciprocal_pole_power",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Diophantine.lean",
      "sha256": "1fc3a7506c70105da8de4c990e860a1f976264bd49c650088f2858d31afa7596",
      "assumptions": [],
      "dependencies": []
    },
    {
      "id": "TangentLimit.summable_abs_tan_div_cube",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Summability.lean",
      "sha256": "0a560016f7f44789f255288ef6d087c18a0f3459d402ce7fc56ebb38036471a9",
      "assumptions": [
        "TangentLimit.PiDiophantine"
      ],
      "dependencies": [
        "TangentLimit.eventual_abs_tan_div_cube_le_rpow"
      ]
    },
    {
      "id": "TangentLimit.summable_abs_tan_div_cube_positive",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Summability.lean",
      "sha256": "ab903c454836df1ecc5d4959a927c91b34359a8393b4d5a571ee8c5a7635be46",
      "assumptions": [
        "TangentLimit.PiDiophantine"
      ],
      "dependencies": [
        "TangentLimit.summable_abs_tan_div_cube"
      ]
    },
    {
      "id": "TangentLimit.summable_abs_tan_div_cube_quotient",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Summability.lean",
      "sha256": "34c431aa6f0e4baad83a0172b130a7fb20121cc0fc00b7210e9472d428b088b3",
      "assumptions": [
        "TangentLimit.PiDiophantine"
      ],
      "dependencies": [
        "TangentLimit.abs_tan_div_cube_eq",
        "TangentLimit.summable_abs_tan_div_cube"
      ]
    },
    {
      "id": "TangentLimit.summable_abs_tan_div_cube_quotient_positive",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Summability.lean",
      "sha256": "c8411a43ea8a80bb9469f318467fa54ae799e1058d526cb716e38fd78939eebf",
      "assumptions": [
        "TangentLimit.PiDiophantine"
      ],
      "dependencies": [
        "TangentLimit.summable_abs_tan_div_cube_quotient"
      ]
    },
    {
      "id": "TangentLimit.summable_tan_div_cube",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Summability.lean",
      "sha256": "349dff7bf1fb9220653a38f161ae074ee795c9e19f430569eb3d605742c3bc6d",
      "assumptions": [
        "TangentLimit.PiDiophantine"
      ],
      "dependencies": [
        "TangentLimit.summable_abs_tan_div_cube_quotient"
      ]
    },
    {
      "id": "TangentLimit.summable_tan_div_cube_positive",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Summability.lean",
      "sha256": "1f3c63bd780ce6194b05d52395ad42c072ea17148887ffc37978946159381e98",
      "assumptions": [
        "TangentLimit.PiDiophantine"
      ],
      "dependencies": [
        "TangentLimit.summable_tan_div_cube"
      ]
    },
    {
      "id": "TangentLimit.tan_div_cube_positive_tendsto_zero",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Limit.lean",
      "sha256": "1f963aa6cd786f6ffd5603103562cea3d8aae619521b99ff157b13d0a561dab4",
      "assumptions": [
        "TangentLimit.PiDiophantine"
      ],
      "dependencies": [
        "TangentLimit.tan_div_cube_tendsto_zero"
      ]
    },
    {
      "id": "TangentLimit.tan_div_cube_tendsto_zero",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Limit.lean",
      "sha256": "ff3ce48922be9a018dba3feb1909c1bd75bf1db9e28b60c9dfd9f9271ec5c6e6",
      "assumptions": [
        "TangentLimit.PiDiophantine"
      ],
      "dependencies": [
        "TangentLimit.eventually_abs_tan_le_quadratic",
        "TangentLimit.tendsto_div_cube_of_eventually_abs_le_sq"
      ]
    },
    {
      "id": "TangentLimit.tan_le_of_cos_lower_bound",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Trigonometry.lean",
      "sha256": "7a96ebea58dd917089b760e36b94bc7ebdbee1baafd754dd5bca868273f03cb9",
      "assumptions": [],
      "dependencies": []
    },
    {
      "id": "TangentLimit.tan_le_of_pole_distance",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Trigonometry.lean",
      "sha256": "f0354c2e53693e29aa0675a50c20d1bfcdfe51f55da0baf3389975f95ed6ee6c",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.chord_cos_bound",
        "TangentLimit.tan_le_of_cos_lower_bound"
      ]
    },
    {
      "id": "TangentLimit.tan_le_pole_power",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/Diophantine.lean",
      "sha256": "c44a1041793fe04fc113d6ce11b55c95c60e16c28a76fa3d6723a59d9c6d9318",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.chord_cos_bound",
        "TangentLimit.pole_distance_lower_bound",
        "TangentLimit.reciprocal_pole_power",
        "TangentLimit.tan_le_of_cos_lower_bound"
      ]
    },
    {
      "id": "TangentLimit.tendsto_div_cube_of_eventually_abs_le_sq",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/LimitComparison.lean",
      "sha256": "422d70c3b10878c0d91be043641a85a80fa3a5388c7a346de797c3a40c6d8280",
      "assumptions": [],
      "dependencies": []
    },
    {
      "id": "TangentLimit.tendsto_div_cube_positive_of_eventually_abs_le_sq",
      "kind": "theorem",
      "source_path": "tangent-limit/TangentLimit/LimitComparison.lean",
      "sha256": "b10dcf8d0a699a8a02c8afefcc82a05ad2279fe4322cbd8ea589bbc224bd4cea",
      "assumptions": [],
      "dependencies": [
        "TangentLimit.tendsto_div_cube_of_eventually_abs_le_sq"
      ]
    }
  ]
};
async function acceptTangent(catalog, readBytes, hashBytes) {
  const snapshot = new Map();
  catalog = (await validate(catalog, async path => {
    const bytes = Uint8Array.from(await readBytes(path));
    snapshot.set(path, bytes); return bytes;
  }, hashBytes)).catalog;
  if (canonicalJSON(catalog.project) !== canonicalJSON(PIN.project)) throw new Error("tangent project pins differ");
  const order = values => values.slice().sort((a,b)=>(a.path||a.id)<(b.path||b.id)?-1:(a.path||a.id)>(b.path||b.id)?1:0);
  if (canonicalJSON(order(catalog.files)) !== canonicalJSON(order(PIN.files))) throw new Error("tangent file pins differ");
  const records = catalog.records.map(r=>({id:r.id,kind:r.kind,source_path:r.statement.source_path,sha256:r.statement.sha256,assumptions:r.assumptions,dependencies:r.dependencies}));
  if (canonicalJSON(order(records)) !== canonicalJSON(order(PIN.records))) throw new Error("tangent record statements, assumptions or dependencies differ");
  for (const record of catalog.records) {
    const source = [{url:PIN.project.repository+"/blob/"+PIN.project.revision+"/"+record.statement.source_path,revision:PIN.project.revision,locator:record.id}];
    if (record.name !== record.id || canonicalJSON(record.sources) !== canonicalJSON(source)) throw new Error("tangent record name or source provenance differs");
  }
  return {accepted:true, revision:PIN.project.revision, records:PIN.records.length, sourceBinding:"exact_published_declaration_text", historicalInventory:inspectHistoricalInventory(snapshot), leanPass:false};
}
function inspectHistoricalInventory(snapshot) {
  const {decodeUTF8} = require("./core.cjs");
  const log = decodeUTF8(snapshot.get("tangent-limit/logs/final-theorem-inventory.log"));
  const names = new Set([...log.matchAll(/^(?:def )?(TangentLimit\.[A-Za-z0-9_]+)(?:\s|:)/gm)].map(m=>m[1]));
  const audits = [...log.matchAll(/'([^']+)' depends on axioms: \[([^\]]*)\]/g)];
  const expected = PIN.records.map(r=>r.id).sort(), observed = [...names].sort();
  if (canonicalJSON(expected) !== canonicalJSON(observed) ||
      audits.length !== expected.length || new Set(audits.map(m=>m[1])).size !== expected.length ||
      canonicalJSON(audits.map(m=>m[1]).sort()) !== canonicalJSON(expected)) throw new Error("historical inventory name coverage mismatch");
  const allowed = new Set(["propext","Classical.choice","Quot.sound"]);
  const axioms = new Set(audits.flatMap(m=>m[2].split(",").map(x=>x.trim()).filter(Boolean)));
  if (log.includes("sorryAx") || [...axioms].some(x=>!allowed.has(x))) throw new Error("historical inventory contains unallowlisted axiom text");
  return {scope:"published_log_content_only", statementNames:names.size, axiomReports:audits.length,
    observedAxiomNames:[...axioms].sort(), liveAxiomInspection:"not_performed"};
}
module.exports = {acceptTangent};

