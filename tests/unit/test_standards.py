"""Unit tests for fuel standards and compliance."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from grades.standards import (
    meets_sulfur_standard,
    meets_cetane_standard,
    meets_octane_standard,
    water_within_limits,
    epa_tier_compliance,
    full_compliance_check,
)


class TestSulfurStandard(unittest.TestCase):
    def test_diesel_pass(self):
        self.assertTrue(meets_sulfur_standard(10, "diesel"))

    def test_diesel_fail(self):
        self.assertFalse(meets_sulfur_standard(20, "diesel"))

    def test_unknown_fuel(self):
        self.assertIsNone(meets_sulfur_standard(10, "unknown"))


class TestCetaneStandard(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(meets_cetane_standard(45))

    def test_fail(self):
        self.assertFalse(meets_cetane_standard(35))


class TestOctaneStandard(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(meets_octane_standard(91))

    def test_fail(self):
        self.assertFalse(meets_octane_standard(85))


class TestWaterLimits(unittest.TestCase):
    def test_within(self):
        self.assertTrue(water_within_limits(0.03))

    def test_exceeded(self):
        self.assertFalse(water_within_limits(0.1))


class TestEpaTier(unittest.TestCase):
    def test_tier3(self):
        self.assertEqual(epa_tier_compliance(5, 0.5), "tier3")

    def test_tier1(self):
        self.assertEqual(epa_tier_compliance(25, 0.8), "tier1")

    def test_non_compliant(self):
        self.assertEqual(epa_tier_compliance(50, 2.0), "non_compliant")


class TestFullCompliance(unittest.TestCase):
    def test_all_pass(self):
        result = full_compliance_check(10, 50, 0.03, 0.005)
        self.assertTrue(all(result.values()))

    def test_some_fail(self):
        result = full_compliance_check(20, 35, 0.1, 0.02)
        self.assertFalse(result["sulfur"])
        self.assertFalse(result["cetane"])


if __name__ == "__main__":
    unittest.main()
