"""Unit tests for statistics module."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from reports.statistics import mean, median, variance, std_dev, percentile


class TestMean(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3.0)

    def test_empty(self):
        self.assertEqual(mean([]), 0.0)

    def test_single(self):
        self.assertEqual(mean([7]), 7.0)


class TestMedian(unittest.TestCase):
    def test_odd(self):
        self.assertEqual(median([1, 3, 5]), 3)

    def test_even(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_empty(self):
        self.assertEqual(median([]), 0.0)


class TestVariance(unittest.TestCase):
    def test_basic(self):
        v = variance([2, 4, 4, 4, 5, 5, 7, 9])
        self.assertAlmostEqual(v, 4.0)

    def test_single(self):
        self.assertEqual(variance([5]), 0.0)


class TestStdDev(unittest.TestCase):
    def test_basic(self):
        s = std_dev([2, 4, 4, 4, 5, 5, 7, 9])
        self.assertAlmostEqual(s, 2.0)


class TestPercentile(unittest.TestCase):
    def test_median(self):
        self.assertEqual(percentile([1, 2, 3, 4, 5], 50), 3)

    def test_min(self):
        self.assertEqual(percentile([1, 2, 3, 4, 5], 0), 1)

    def test_max(self):
        self.assertEqual(percentile([1, 2, 3, 4, 5], 100), 5)

    def test_empty(self):
        self.assertEqual(percentile([], 50), 0.0)


if __name__ == "__main__":
    unittest.main()
