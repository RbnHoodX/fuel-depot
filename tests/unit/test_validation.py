"""Unit tests for validation utilities."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from utils.validation import (
    is_positive,
    is_non_negative,
    is_valid_name,
    is_valid_kind,
    validate_transfer_args,
    clamp,
)


class TestIsPositive(unittest.TestCase):
    def test_positive_int(self):
        self.assertTrue(is_positive(5))

    def test_zero(self):
        self.assertFalse(is_positive(0))

    def test_negative(self):
        self.assertFalse(is_positive(-1))

    def test_string(self):
        self.assertFalse(is_positive("5"))


class TestIsNonNegative(unittest.TestCase):
    def test_zero(self):
        self.assertTrue(is_non_negative(0))

    def test_positive(self):
        self.assertTrue(is_non_negative(10))

    def test_negative(self):
        self.assertFalse(is_non_negative(-0.01))


class TestIsValidName(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_valid_name("main"))

    def test_empty(self):
        self.assertFalse(is_valid_name(""))

    def test_spaces_only(self):
        self.assertFalse(is_valid_name("   "))

    def test_leading_space(self):
        self.assertFalse(is_valid_name(" main"))

    def test_non_string(self):
        self.assertFalse(is_valid_name(123))


class TestIsValidKind(unittest.TestCase):
    def test_standard(self):
        self.assertTrue(is_valid_kind("standard"))

    def test_reserve(self):
        self.assertTrue(is_valid_kind("reserve"))

    def test_invalid(self):
        self.assertFalse(is_valid_kind("overflow"))


class TestValidateTransferArgs(unittest.TestCase):
    def test_valid(self):
        errors = validate_transfer_args("a", "b", 100)
        self.assertEqual(errors, [])

    def test_same_source_dest(self):
        errors = validate_transfer_args("a", "a", 100)
        self.assertIn("source and destination must differ", errors)

    def test_invalid_amount(self):
        errors = validate_transfer_args("a", "b", -1)
        self.assertIn("amount must be positive", errors)


class TestClamp(unittest.TestCase):
    def test_within_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_below(self):
        self.assertEqual(clamp(-5, 0, 10), 0)

    def test_above(self):
        self.assertEqual(clamp(15, 0, 10), 10)


if __name__ == "__main__":
    unittest.main()
