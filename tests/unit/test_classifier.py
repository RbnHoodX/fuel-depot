"""Unit tests for fuel classification functions."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from grades.classifier import (
    octane_grade,
    viscosity_band,
    sulfur_level,
    cetane_quality,
    flash_point_safety,
    water_content_rating,
)


class TestOctaneGrade(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(octane_grade(87), "regular")

    def test_midgrade(self):
        self.assertEqual(octane_grade(91), "midgrade")

    def test_premium(self):
        self.assertEqual(octane_grade(95), "premium")

    def test_racing(self):
        self.assertEqual(octane_grade(100), "racing")

    def test_unknown(self):
        self.assertEqual(octane_grade(50), "unknown")

    def test_non_numeric(self):
        self.assertEqual(octane_grade("high"), "unknown")


class TestViscosityBand(unittest.TestCase):
    def test_thin(self):
        self.assertEqual(viscosity_band(1.0), "thin")

    def test_heavy(self):
        self.assertEqual(viscosity_band(15.0), "heavy")

    def test_unclassed(self):
        self.assertEqual(viscosity_band(200.0), "unclassed")


class TestSulfurLevel(unittest.TestCase):
    def test_ultra_low(self):
        self.assertEqual(sulfur_level(5), "ultra-low")

    def test_low(self):
        self.assertEqual(sulfur_level(30), "low")

    def test_regular(self):
        self.assertEqual(sulfur_level(100), "regular")

    def test_high(self):
        self.assertEqual(sulfur_level(600), "high")

    def test_invalid(self):
        self.assertEqual(sulfur_level(-1), "invalid")


class TestCetaneQuality(unittest.TestCase):
    def test_poor(self):
        self.assertEqual(cetane_quality(35), "poor")

    def test_good(self):
        self.assertEqual(cetane_quality(50), "good")

    def test_excellent(self):
        self.assertEqual(cetane_quality(60), "excellent")


class TestFlashPointSafety(unittest.TestCase):
    def test_extremely_flammable(self):
        self.assertEqual(flash_point_safety(-43), "extremely_flammable")

    def test_flammable(self):
        self.assertEqual(flash_point_safety(38), "flammable")

    def test_combustible(self):
        self.assertEqual(flash_point_safety(80), "combustible")

    def test_non_flammable(self):
        self.assertEqual(flash_point_safety(100), "non_flammable")


class TestWaterContentRating(unittest.TestCase):
    def test_dry(self):
        self.assertEqual(water_content_rating(0.01), "dry")

    def test_contaminated(self):
        self.assertEqual(water_content_rating(0.2), "contaminated")


if __name__ == "__main__":
    unittest.main()
