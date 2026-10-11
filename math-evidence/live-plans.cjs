"use strict";
// Fixed inspected plans, not imported records. Adding a plan requires code review.
const PLANS={
  "custom-axiom": {
    "definitionHarness": null,
    "modules": [
      {
        "destination": "ReceiptFixture.lean",
        "module": "ReceiptFixture",
        "source": "fixtures/CustomAxiom.lean"
      }
    ],
    "projectFiles": [],
    "replayHarness": "lean/expected/sorry-replay.lean",
    "targets": [
      {
        "kind": "theorem",
        "name": "ReceiptFixture.incomplete"
      }
    ],
    "toolkitFiles": [
      "fixtures/CustomAxiom.lean",
      "lean/EvidenceHarness.lean",
      "lean/expected/sorry-types.lean",
      "lean/expected/sorry-replay.lean"
    ],
    "typeHarness": "lean/expected/sorry-types.lean"
  },
  "general": {
    "definitionHarness": null,
    "modules": [
      {
        "destination": "ReceiptFixture.lean",
        "module": "ReceiptFixture",
        "source": "fixtures/General.lean"
      }
    ],
    "projectFiles": [],
    "replayHarness": "lean/expected/general-replay.lean",
    "targets": [
      {
        "kind": "theorem",
        "name": "ReceiptFixture.general"
      }
    ],
    "toolkitFiles": [
      "fixtures/General.lean",
      "lean/EvidenceHarness.lean",
      "lean/expected/general-types.lean",
      "lean/expected/general-replay.lean"
    ],
    "typeHarness": "lean/expected/general-types.lean"
  },
  "skip-kernel": {
    "definitionHarness": null,
    "modules": [
      {
        "destination": "ReceiptFixture.lean",
        "module": "ReceiptFixture",
        "source": "fixtures/SkipKernel.lean"
      }
    ],
    "projectFiles": [],
    "replayHarness": "lean/expected/sorry-replay.lean",
    "targets": [
      {
        "kind": "theorem",
        "name": "ReceiptFixture.incomplete"
      }
    ],
    "toolkitFiles": [
      "fixtures/SkipKernel.lean",
      "lean/EvidenceHarness.lean",
      "lean/expected/sorry-types.lean",
      "lean/expected/sorry-replay.lean"
    ],
    "typeHarness": "lean/expected/sorry-types.lean"
  },
  "sorry": {
    "definitionHarness": null,
    "modules": [
      {
        "destination": "ReceiptFixture.lean",
        "module": "ReceiptFixture",
        "source": "fixtures/Sorry.lean"
      }
    ],
    "projectFiles": [],
    "replayHarness": "lean/expected/sorry-replay.lean",
    "targets": [
      {
        "kind": "theorem",
        "name": "ReceiptFixture.incomplete"
      }
    ],
    "toolkitFiles": [
      "fixtures/Sorry.lean",
      "lean/EvidenceHarness.lean",
      "lean/expected/sorry-types.lean",
      "lean/expected/sorry-replay.lean"
    ],
    "typeHarness": "lean/expected/sorry-types.lean"
  },
  "specialized": {
    "definitionHarness": null,
    "modules": [
      {
        "destination": "ReceiptFixture.lean",
        "module": "ReceiptFixture",
        "source": "fixtures/General.lean"
      }
    ],
    "projectFiles": [],
    "replayHarness": "lean/expected/general-replay.lean",
    "targets": [
      {
        "kind": "theorem",
        "name": "ReceiptFixture.general"
      }
    ],
    "toolkitFiles": [
      "fixtures/General.lean",
      "lean/EvidenceHarness.lean",
      "lean/expected/specialized-types.lean",
      "lean/expected/general-replay.lean"
    ],
    "typeHarness": "lean/expected/specialized-types.lean"
  },
  "tangent": {
    "definitionHarness": "lean/expected/tangent-definitions.lean",
    "modules": [
      {
        "destination": "TangentLimit/Hypothesis.lean",
        "module": "TangentLimit.Hypothesis",
        "source": "tangent-limit/TangentLimit/Hypothesis.lean"
      },
      {
        "destination": "TangentLimit/LimitComparison.lean",
        "module": "TangentLimit.LimitComparison",
        "source": "tangent-limit/TangentLimit/LimitComparison.lean"
      },
      {
        "destination": "TangentLimit/NonPole.lean",
        "module": "TangentLimit.NonPole",
        "source": "tangent-limit/TangentLimit/NonPole.lean"
      },
      {
        "destination": "TangentLimit/NearestPole.lean",
        "module": "TangentLimit.NearestPole",
        "source": "tangent-limit/TangentLimit/NearestPole.lean"
      },
      {
        "destination": "TangentLimit/Trigonometry.lean",
        "module": "TangentLimit.Trigonometry",
        "source": "tangent-limit/TangentLimit/Trigonometry.lean"
      },
      {
        "destination": "TangentLimit/Diophantine.lean",
        "module": "TangentLimit.Diophantine",
        "source": "tangent-limit/TangentLimit/Diophantine.lean"
      },
      {
        "destination": "TangentLimit/Limit.lean",
        "module": "TangentLimit.Limit",
        "source": "tangent-limit/TangentLimit/Limit.lean"
      },
      {
        "destination": "TangentLimit/Summability.lean",
        "module": "TangentLimit.Summability",
        "source": "tangent-limit/TangentLimit/Summability.lean"
      },
      {
        "destination": "TangentLimit.lean",
        "module": "TangentLimit",
        "source": "tangent-limit/TangentLimit.lean"
      }
    ],
    "projectFiles": [
      {
        "path": "tangent-limit/README.md",
        "role": "source",
        "sha256": "5be38954d69d42c1a0fb6a109983574b728b88c361af32cc9cb0d48e627f295a"
      },
      {
        "path": "tangent-limit/TangentLimit.lean",
        "role": "source",
        "sha256": "98c74e84ab564605a18c9cb87fb6112f8b7bf999349dfba1f9e3ead868faac02"
      },
      {
        "path": "tangent-limit/TangentLimit/Diophantine.lean",
        "role": "source",
        "sha256": "74116a224783c4d91265c73f276eab0e280f5d047c3cb32260ee10a6204807bf"
      },
      {
        "path": "tangent-limit/TangentLimit/Hypothesis.lean",
        "role": "source",
        "sha256": "6f9fb3e7a25e2ba27fba29faf93e88add77a8c0aa3a8de59be72ae7b9ea2562a"
      },
      {
        "path": "tangent-limit/TangentLimit/Limit.lean",
        "role": "source",
        "sha256": "05ea71aef2541bdc9137c8dd110c3d11d8e2ffc5b851e931aeeef027fdfb0336"
      },
      {
        "path": "tangent-limit/TangentLimit/LimitComparison.lean",
        "role": "source",
        "sha256": "9250070b23a25f76ad620c8fee0b353ffc5b04b5823177e4bf6b92a28473813c"
      },
      {
        "path": "tangent-limit/TangentLimit/NearestPole.lean",
        "role": "source",
        "sha256": "b6321c174149a6e7f264d1d31b4813954dfba14900b9ab15c21c4701a3dc4cec"
      },
      {
        "path": "tangent-limit/TangentLimit/NonPole.lean",
        "role": "source",
        "sha256": "3ca47fd29a14a8e1299782ed729f96252a6768a84c67742bc075fb1273496710"
      },
      {
        "path": "tangent-limit/TangentLimit/Summability.lean",
        "role": "source",
        "sha256": "b6308da63a70ae2e7d45719afc2a5af71935061f8c9ec383740010a3613bf273"
      },
      {
        "path": "tangent-limit/TangentLimit/Trigonometry.lean",
        "role": "source",
        "sha256": "169ede182499acaf928a19eacb4605c32c0f71a52e17ae7edc0e26912eb40039"
      },
      {
        "path": "tangent-limit/docs/SOURCES.md",
        "role": "source",
        "sha256": "fd1e849579926531aac21e4f5743e1c8d6460740c1bc9ecbdde6a050f67473c7"
      },
      {
        "path": "tangent-limit/docs/independent-review.md",
        "role": "review",
        "sha256": "5026dedb437641910b1583a8d81121457ef1755e79e7558f461d0d0f8d07f2eb"
      },
      {
        "path": "tangent-limit/docs/mathematical-proof.md",
        "role": "source",
        "sha256": "f52aa95b1c5829f26d1c72c4aa244b6fde7e9491f61d01dd52b9ebffd67d93d1"
      },
      {
        "path": "tangent-limit/docs/theorem-statements.md",
        "role": "statement_inventory",
        "sha256": "aeade1452a9747b370e4c9b67cdcdeba14a6fab9915f7716c18ffb869533ae34"
      },
      {
        "path": "tangent-limit/docs/verification-summary.json",
        "role": "legacy_log",
        "sha256": "dbeb8a2389d6fb0f549e433f6484b013ded7a755de5888be0fcdb01917e09af6"
      },
      {
        "path": "tangent-limit/lake-manifest.json",
        "role": "lockfile",
        "sha256": "8f871ddcf1917c176ac801f24bc66c975e4562d4d7aab8193c45ef7f31d5ad03"
      },
      {
        "path": "tangent-limit/lakefile.toml",
        "role": "source",
        "sha256": "dbb3f4f563156a8062f93ceb0aa660a12b60650d2f47fb0de4f32308fb25e451"
      },
      {
        "path": "tangent-limit/lean-toolchain",
        "role": "toolchain",
        "sha256": "42779d67b81608af8a12aa4328d2ab47ca201925b3b2bd68369587b5340bb434"
      },
      {
        "path": "tangent-limit/logs/final-build.log",
        "role": "legacy_log",
        "sha256": "0a34f9325b605efffd2947f7345a15c0dcfb9ec5d86aedbeb512aebe3bf67524"
      },
      {
        "path": "tangent-limit/logs/final-theorem-inventory.log",
        "role": "legacy_log",
        "sha256": "b6e66b3382e58831c6972b116617ada1d308f9d1157399d6fa96f124ad96ad57"
      },
      {
        "path": "tangent-limit/logs/source-audit.log",
        "role": "legacy_log",
        "sha256": "77b40abe9cb9340a20700fcf5fa745f233c5afe8724ebda3a4e7574360b2763d"
      },
      {
        "path": "tangent-limit/scripts/TheoremInventory.lean",
        "role": "source",
        "sha256": "0a5e8810ccc28e617482e5cd9ca9bf72f69d98e4e50651bd09488450a1993fa9"
      },
      {
        "path": "tangent-limit/scripts/build.sh",
        "role": "source",
        "sha256": "fbb7dcd71745678a3f18875cd75139db615be6377c14658641db52dcd8a40b1b"
      },
      {
        "path": "tangent-limit/scripts/environment.sh",
        "role": "source",
        "sha256": "701d4155694efb2b3893f01b20f3a496224ffea91f6595b60dcc4392eaf4e373"
      },
      {
        "path": "tangent-limit/scripts/setup.sh",
        "role": "source",
        "sha256": "e2a8c6ce4c6af2fd7387be5a043694cc017b8af4bad6fe143b3f03f819bd5e9b"
      },
      {
        "path": "tangent-limit/scripts/verify.sh",
        "role": "source",
        "sha256": "d9d5890f76eda58e5451ff320f8315cd54ee491938ca9c7f4b61f6853b881fa1"
      }
    ],
    "replayHarness": "lean/expected/tangent-replay.lean",
    "targets": [
      {
        "kind": "assumption",
        "name": "TangentLimit.PiDiophantine"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.abs_cos_eq_abs_sin_offset"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.abs_poleOffset_le"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.abs_tan_div_cube_eq"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.chord_cos_bound"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.cos_intCast_ne_zero"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.cos_natCast_ne_zero"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.eventual_abs_tan_div_cube_le_rpow"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.eventually_abs_tan_le_quadratic"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.eventually_poleDenom_ge"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.eventually_tan_le_pole_rpow"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.lt_poleIndex_add_one_mul_pi"
      },
      {
        "kind": "definition",
        "name": "TangentLimit.poleDenom"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.poleDenom_le_two_mul"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.poleDenom_odd"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.poleDenom_pos"
      },
      {
        "kind": "definition",
        "name": "TangentLimit.poleIndex"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.poleIndex_mul_pi_le"
      },
      {
        "kind": "definition",
        "name": "TangentLimit.poleOffset"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.poleOffset_nearest"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.pole_distance_identity"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.pole_distance_lower_bound"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.pole_distance_lower_bound_of_piDiophantine"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.reciprocal_pole_power"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.summable_abs_tan_div_cube"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.summable_abs_tan_div_cube_positive"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.summable_abs_tan_div_cube_quotient"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.summable_abs_tan_div_cube_quotient_positive"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.summable_tan_div_cube"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.summable_tan_div_cube_positive"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.tan_div_cube_positive_tendsto_zero"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.tan_div_cube_tendsto_zero"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.tan_le_of_cos_lower_bound"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.tan_le_of_pole_distance"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.tan_le_pole_power"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.tendsto_div_cube_of_eventually_abs_le_sq"
      },
      {
        "kind": "theorem",
        "name": "TangentLimit.tendsto_div_cube_positive_of_eventually_abs_le_sq"
      }
    ],
    "toolkitFiles": [
      "lean/EvidenceHarness.lean",
      "lean/expected/tangent-types.lean",
      "lean/expected/tangent-definitions.lean",
      "lean/expected/tangent-replay.lean"
    ],
    "typeHarness": "lean/expected/tangent-types.lean"
  },
  "valid": {
    "definitionHarness": null,
    "modules": [
      {
        "destination": "ReceiptFixture.lean",
        "module": "ReceiptFixture",
        "source": "fixtures/Valid.lean"
      }
    ],
    "projectFiles": [],
    "replayHarness": "lean/expected/valid-replay.lean",
    "targets": [
      {
        "kind": "theorem",
        "name": "ReceiptFixture.valid"
      }
    ],
    "toolkitFiles": [
      "fixtures/Valid.lean",
      "lean/EvidenceHarness.lean",
      "lean/expected/valid-types.lean",
      "lean/expected/valid-replay.lean"
    ],
    "typeHarness": "lean/expected/valid-types.lean"
  },
  "wrong": {
    "definitionHarness": null,
    "modules": [
      {
        "destination": "ReceiptFixture.lean",
        "module": "ReceiptFixture",
        "source": "fixtures/Valid.lean"
      }
    ],
    "projectFiles": [],
    "replayHarness": "lean/expected/valid-replay.lean",
    "targets": [
      {
        "kind": "theorem",
        "name": "ReceiptFixture.valid"
      }
    ],
    "toolkitFiles": [
      "fixtures/Valid.lean",
      "lean/EvidenceHarness.lean",
      "lean/expected/wrong-types.lean",
      "lean/expected/valid-replay.lean"
    ],
    "typeHarness": "lean/expected/wrong-types.lean"
  },
  "wrong-compilation": {
    "definitionHarness": null,
    "modules": [
      {
        "destination": "ReceiptFixture.lean",
        "module": "ReceiptFixture",
        "source": "fixtures/WrongStatement.lean"
      }
    ],
    "projectFiles": [],
    "replayHarness": "lean/expected/valid-replay.lean",
    "targets": [
      {
        "kind": "theorem",
        "name": "ReceiptFixture.valid"
      }
    ],
    "toolkitFiles": [
      "fixtures/WrongStatement.lean",
      "lean/EvidenceHarness.lean",
      "lean/expected/wrong-types.lean",
      "lean/expected/valid-replay.lean"
    ],
    "typeHarness": "lean/expected/wrong-types.lean"
  }
};
const TRUSTED_FILES={
  "fixtures/CustomAxiom.lean": "b27f1b88e91e6398afd0515888f9989cfd9621dc1760c9f4a04558e019ad745c",
  "fixtures/General.lean": "5672629432188e7f8ed63905814d88383b98d350e8682f4b53628e22369839c0",
  "fixtures/SkipKernel.lean": "9695f9fbffab76e98dcf7c861ffb7b2c6299722ea214616043521378394f08c4",
  "fixtures/Sorry.lean": "ea0e01152043399b03973199cfe70fa9a07dc6e5f2b9ac0911ce255f7881f04d",
  "fixtures/Valid.lean": "c51edb193973c7a218bdb325d1962d64b0426144bf0d900eb808767bcf28c720",
  "fixtures/WrongStatement.lean": "d95004e9acb672677008a69cd8854f16933b071abbeff8796387ff8bc069d13c",
  "lean/EvidenceHarness.lean": "bb71282fcb088498a9c40b0460694f1663e8f3a145fc15469050b8ade2f390dc",
  "lean/expected/general-replay.lean": "89fe8a60887223c2b772b9c6e30f6f221b8540234479e67afb97e8da519a75ac",
  "lean/expected/general-types.lean": "667f3bfc0292ab9fd237d34ad567275eaac36dcc605d845a55d43fb1856becce",
  "lean/expected/sorry-replay.lean": "a82858bc9f4f46be3e8c62a4e1d64e6f7eb220210d98180258f4f9dcbef0a778",
  "lean/expected/sorry-types.lean": "7d77341c740d25e2baaf32fd89417f44c467ada81383d60c1a11743ddaff7e8b",
  "lean/expected/specialized-types.lean": "ce0337b8d7117b8dcc510bbc853e677599323e55b948e5a196015cdf883617b4",
  "lean/expected/tangent-definitions.lean": "852eece59fe507c9d536699170113aef030b14c05bcd643a15445c37ee42ce82",
  "lean/expected/tangent-replay.lean": "46bc3355d4b7a477553058fad71fe1445bd679ecf5cbf2e7077301c88ed465f0",
  "lean/expected/tangent-types.lean": "d309349a45ff46eec8b27678940907d6474755c861095269bebbc203eb867493",
  "lean/expected/valid-replay.lean": "4489acf51b153fefcc1074fcf1170ff653933f30cced88ef9d55f9a8374cb7a9",
  "lean/expected/valid-types.lean": "abf865f6ef62f8f8744fa7d946ffebffa6ed73a4bbf7ae7620d963531a267393",
  "lean/expected/wrong-types.lean": "4eae327ccae32975acf5cd9a18e173b25a44ca2040773918bdc2074dbee892ba"
};
module.exports={PLANS,TRUSTED_FILES};
