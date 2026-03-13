"""Unit tests for formatting utilities."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from utils.formatting import (
    pad_left,
    pad_right,
    truncate,
    title_case,
    slugify,
    format_units,
    pluralize,
    join_names,
)


class TestPadding(unittest.TestCase):
    def test_pad_left(self):
        self.assertEqual(pad_left("hi", 5), "   hi")

    def test_pad_right(self):
        self.assertEqual(pad_right("hi", 5), "hi   ")


class TestTruncate(unittest.TestCase):
    def test_short_unchanged(self):
        self.assertEqual(truncate("hello", 10), "hello")

    def test_long_truncated(self):
        self.assertEqual(truncate("hello world", 8), "hello...")


class TestTitleCase(unittest.TestCase):
    def test_underscore(self):
        self.assertEqual(title_case("fuel_depot"), "Fuel Depot")

    def test_hyphen(self):
        self.assertEqual(title_case("main-storage"), "Main Storage")


class TestSlugify(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Fuel Depot"), "fuel-depot")

    def test_underscores(self):
        self.assertEqual(slugify("main_tank"), "main-tank")


class TestFormatUnits(unittest.TestCase):
    def test_default(self):
        self.assertEqual(format_units(100), "100.00 units")

    def test_custom(self):
        self.assertEqual(format_units(3.5, "liters", 1), "3.5 liters")


class TestPluralize(unittest.TestCase):
    def test_singular(self):
        self.assertEqual(pluralize("tank", 1), "tank")

    def test_plural(self):
        self.assertEqual(pluralize("tank", 2), "tanks")

    def test_ends_in_s(self):
        self.assertEqual(pluralize("bus", 2), "buses")


class TestJoinNames(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(join_names([]), "")

    def test_single(self):
        self.assertEqual(join_names(["alpha"]), "alpha")

    def test_two(self):
        self.assertEqual(join_names(["alpha", "beta"]), "alpha and beta")

    def test_three(self):
        self.assertEqual(join_names(["a", "b", "c"]), "a, b, and c")


if __name__ == "__main__":
    unittest.main()
