"""Independent regression checks for geometry, certificates, and scope guards."""

from fractions import Fraction as F
import importlib.util
from pathlib import Path
import sys
import unittest


SCRIPT = Path(__file__).resolve().parents[1]/"scripts"/"check_exact.py"
SPEC = importlib.util.spec_from_file_location("transport_exact", SCRIPT)
exact = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = exact
SPEC.loader.exec_module(exact)


def clipped_central_mass_from_slices(a, b):
    """Independent integration of clamp(a+bt,0,1) against dt/2.

    This method neither clips polygons nor uses the claimed joint matrix.
    Its exact trapezoids are valid because all changes of affine expression
    occur at the explicitly inserted rational breakpoints.
    """
    breakpoints = [F(-1), F(1)]
    if b:
        breakpoints += [crossing for crossing in (-a/b, (1-a)/b)
                        if -1 < crossing < 1]
    breakpoints = sorted(set(breakpoints))
    width = lambda t: max(F(0), min(F(1), a+b*t))
    return sum(((right-left)*(width(left)+width(right))/4
                for left, right in zip(breakpoints, breakpoints[1:])), F(0))


class GeometryTests(unittest.TestCase):
    def test_all_affine_comparisons_are_derived(self):
        u, v = exact.potentials(F(1,4), F(1,8))
        self.assertEqual(exact.derive_cells(u),
                         [[(F(-1), F(0), F(-1,4)), (F(-2), F(0), F(0))],
                          [(F(1), F(0), F(1,4)), (F(-1), F(0), F(1,4))],
                          [(F(2), F(0), F(0)), (F(1), F(0), F(-1,4))]])
        self.assertEqual(exact.derive_cells(v)[1],
                         [(F(1), F(1,8), F(1,4)),
                          (F(-1), F(1,8), F(1,4))])

    def test_clipping_empty_boundary_and_quadrant(self):
        self.assertEqual(exact.polygon_area(exact.intersect_polygon([(F(1),F(0),F(-2))])), 0)
        self.assertEqual(exact.polygon_area(exact.intersect_polygon([(F(1),F(0),F(-1))])), 0)
        self.assertEqual(exact.polygon_area(exact.intersect_polygon([(F(1),F(1),F(0))])), 2)
        self.assertEqual(exact.polygon_area(exact.intersect_polygon(
            [(F(1),F(0),F(0)), (F(0),F(1),F(0))])), 1)

    def test_original_case_values(self):
        result = exact.check_case(F(1,4), F(1,8))
        self.assertEqual(result["common_source_joint_mass_matrix"],
                         [[F(23,64), F(1,64), F(0)],
                          [F(1,64), F(7,32), F(1,64)],
                          [F(0), F(1,64), F(23,64)]])
        self.assertEqual(result["W2_squared"], F(1,256))
        self.assertEqual(result["L2_map_difference_squared"], F(17,256))
        self.assertEqual(result["distinct_vertices_enumerated"], 10)

    def test_equal_masses_have_six_vertices(self):
        result = exact.check_case(F(1,3), F(1,6))
        self.assertEqual(result["distinct_vertices_enumerated"], 6)
        self.assertEqual(result["W2_squared"], F(1,108))

    def test_independent_clipped_slice_integrals(self):
        for a, b, expected in ((F(1,4), F(1,2), F(9,32)),
                               (F(3,4), F(1,2), F(23,32)),
                               (F(3,5), F(399,1000), F(3,5)),
                               (F(1,4), F(-1,2), F(9,32))):
            with self.subTest(a=a, b=b):
                central = exact.common_source_geometry(a,b)["v_masses"][1]
                self.assertEqual(central, expected)
                self.assertEqual(central, clipped_central_mass_from_slices(a,b))

    def test_slice_integral_all_small_rationals(self):
        for a in (F(1,7), F(1,4), F(1,2), F(3,4), F(8,9)):
            for b in (F(-2,3), F(-1,8), F(0), F(1,8), F(2,3)):
                with self.subTest(a=a,b=b):
                    central = exact.common_source_geometry(a,b)["v_masses"][1]
                    self.assertEqual(central, clipped_central_mass_from_slices(a,b))

    def test_scope_and_float_guards(self):
        for a, b in ((F(1,4),F(0)), (F(1,4),F(-1,8)),
                     (F(1,4),F(1,4)), (F(3,4),F(1,4)), (F(3,4),F(1,2))):
            with self.subTest(a=a,b=b), self.assertRaises(ValueError):
                exact.check_case(a,b)
        with self.assertRaises(ValueError):
            exact.check_case(0.25, "1/8")
        with self.assertRaises(ValueError):
            exact.derive_cells([exact.Affine((F(0),F(0)),F(0)),
                                exact.Affine((F(0),F(0)),F(1))])


class CertificateTests(unittest.TestCase):
    def setUp(self):
        self.a, self.b = F(1,4), F(1,8)
        self.result = exact.check_case(self.a,self.b,even_ps=(2,),enumerate_vertices=False)
        self.masses = self.result["atom_masses"]
        self.costs = self.result["quadratic_cost_matrix"]
        self.primal = [[self.masses[i] if i==j else F(0) for j in range(3)]
                       for i in range(3)]

    def test_matching_primal_dual_certificate(self):
        certificate = exact.verify_primal_dual(self.costs, self.masses, self.primal,
                                               [F(0)]*3, [F(0),self.b**2,F(0)])
        self.assertEqual(certificate["primal_objective"], F(1,256))
        self.assertEqual(certificate["dual_slack_matrix"],
                         [[F(0),F(1),F(4)], [F(1),F(0),F(1)], [F(4),F(1),F(0)]])

    def test_bad_marginal_and_negative_mass_rejected(self):
        wrong = [row.copy() for row in self.primal]
        wrong[0][0] += F(1,100)
        with self.assertRaises(ValueError):
            exact.verify_coupling(wrong,self.masses,self.masses)
        wrong[0][1] = F(-1,100)
        with self.assertRaises(ValueError):
            exact.verify_coupling(wrong,self.masses,self.masses)

    def test_bad_dual_rejected(self):
        with self.assertRaises(ValueError):
            exact.verify_primal_dual(self.costs,self.masses,self.primal,
                                    [F(0)]*3,[F(0),2*self.b**2,F(0)])
        with self.assertRaises(ValueError):
            exact.verify_primal_dual(self.costs,self.masses,self.primal,
                                    [F(0)]*3,[F(0),F(0),F(0)])

    def test_even_p_certificates_and_unsupported_odd_p(self):
        for p in (2,4,6,8,10):
            certificate = exact.check_even_p(self.a,self.b,p,self.costs,self.masses)
            self.assertEqual(certificate["Wp_to_the_p"], self.a*self.b**p)
            self.assertTrue(certificate["unique_by_positive_off_diagonal_slack"])
        with self.assertRaises(ValueError):
            exact.check_even_p(self.a,self.b,3,self.costs,self.masses)


class ExponentTests(unittest.TestCase):
    def test_W2_endpoint_power(self):
        result = exact.exact_ratio_power(F(1,4),F(1,8),2,F(1,3))
        self.assertEqual(result["ratio_power"], 6)
        self.assertEqual(result["ratio_to_integer_power"], F(4913,65536))

    def test_fixed_mass_endpoint_power(self):
        result = exact.exact_ratio_power(F(1,4),F(1,32),2,F(1,2))
        self.assertEqual(result["ratio_power"], 4)
        self.assertEqual(result["ratio_to_integer_power"], F(4225,4096))

    def test_rational_p_clears_denominators(self):
        result = exact.exact_ratio_power(F(1,4),F(1,8),F(3,2),F(3,10))
        self.assertEqual(result["ratio_power"], 10)
        self.assertEqual(result["a_denominator_power"], 2)
        self.assertEqual(result["b_denominator_power"], 3)
        self.assertEqual(result["ratio_to_integer_power"], F(17**5,2**27))

    def test_actual_candidate_constant_violations(self):
        for family, p, alpha in (("shrinking_mass",F(2),F(1,2)),
                                  ("shrinking_mass",F(3,2),F(2,5)),
                                  ("fixed_mass",F(2),F(3,5))):
            with self.subTest(family=family,p=p,alpha=alpha):
                witness = exact.counterexample_witness(p,alpha,F(100),family)
                self.assertGreater(witness["numerator"],
                                   witness["denominator"] * 100**witness["ratio_power"])

    def test_endpoint_and_subcritical_claims_rejected(self):
        for family, alpha in (("shrinking_mass",F(1,3)),
                               ("shrinking_mass",F(1,4)),
                               ("fixed_mass",F(1,2)), ("fixed_mass",F(1,3))):
            with self.subTest(family=family,alpha=alpha), self.assertRaises(ValueError):
                exact.counterexample_witness(2,alpha,1,family)


if __name__ == "__main__":
    unittest.main()
