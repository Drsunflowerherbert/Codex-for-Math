"""Regenerate our bounded data and Paley checks, without network access."""

import hashlib
import json
from pathlib import Path

from enumerate_williamson import study
from hadamard import is_prime, paley_prime, sign_bytes, verify


ROOT = Path(__file__).resolve().parents[1]


def main():
    results = []
    for p in range(3, 200, 4):
        if is_prime(p):
            matrix = paley_prime(p)
            results.append({"prime": p, **verify(matrix),
                            "canonical_sign_bytes_sha256": hashlib.sha256(sign_bytes(matrix)).hexdigest()})
    paley = {"family": "Paley type I over prime field, fixed sign convention",
             "complete_for_primes_p_at_most": 199,
             "prime_congruence_mod_4": 3, "results": results}
    (ROOT / "evidence/paley-primes-through-199.json").write_text(
        json.dumps(paley, indent=2, sort_keys=True) + "\n")
    williamson = {"family": "symmetric circulant Williamson; s[0]=+1; block multiset",
              "complete_for_odd_core_orders": list(range(1, 16, 2)),
              "arithmetic": "exact Python integers; all complementary PAF pair buckets",
              "results": [study(m) for m in range(1, 16, 2)]}
    (ROOT / "data/williamson-odd-through-15.json").write_text(
        json.dumps(williamson, indent=2, sort_keys=True) + "\n")
    print(f"Verified {len(results)} Paley matrices; {sum(r['unordered_row_pairs_checked'] for r in results)} row pairs")
    print("Complete normalized symmetric Williamson enumeration for odd m=1,...,15")
    for r in williamson["results"]:
        print(f"m={r['core_order']}: {r['normalized_sequence_multisets_solving_PAF']} multisets; "
              f"{len(r['realized_types_with_one_verified_witness_each'])} row-sum types")


if __name__ == "__main__":
    main()
