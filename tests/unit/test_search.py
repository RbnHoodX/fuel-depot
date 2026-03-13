"""Unit tests for search utilities."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tank import Tank
from dispatch import Dispatch, DispatchLog
from utils.search import (
    find_tanks_by_kind,
    find_tanks_with_fuel,
    find_empty_tanks,
    find_tank_by_name,
    search_tanks_by_prefix,
    filter_dispatches_by_amount,
    dispatches_involving,
)


class TestFindTanksByKind(unittest.TestCase):
    def test_filter_standard(self):
        tanks = [Tank("a", "standard"), Tank("b", "reserve"), Tank("c", "standard")]
        result = find_tanks_by_kind(tanks, "standard")
        self.assertEqual(len(result), 2)

    def test_filter_empty(self):
        tanks = [Tank("a", "standard")]
        result = find_tanks_by_kind(tanks, "reserve")
        self.assertEqual(len(result), 0)


class TestFindTanksWithFuel(unittest.TestCase):
    def test_with_dispatches(self):
        a = Tank("a")
        b = Tank("b")
        log = DispatchLog()
        log.record(Dispatch(a, b, 100))
        result = find_tanks_with_fuel([a, b])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "a")


class TestFindEmptyTanks(unittest.TestCase):
    def test_no_dispatches(self):
        tanks = [Tank("a"), Tank("b")]
        result = find_empty_tanks(tanks)
        self.assertEqual(len(result), 2)


class TestFindTankByName(unittest.TestCase):
    def test_found(self):
        tanks = [Tank("a"), Tank("b")]
        self.assertEqual(find_tank_by_name(tanks, "b").name, "b")

    def test_not_found(self):
        tanks = [Tank("a")]
        self.assertIsNone(find_tank_by_name(tanks, "z"))


class TestSearchByPrefix(unittest.TestCase):
    def test_prefix(self):
        tanks = [Tank("main-a"), Tank("main-b"), Tank("reserve")]
        result = search_tanks_by_prefix(tanks, "main")
        self.assertEqual(len(result), 2)


class TestFilterDispatchesByAmount(unittest.TestCase):
    def test_min_amount(self):
        a = Tank("a")
        b = Tank("b")
        dispatches = [Dispatch(a, b, 50), Dispatch(a, b, 150), Dispatch(a, b, 200)]
        result = filter_dispatches_by_amount(dispatches, min_amount=100)
        self.assertEqual(len(result), 2)

    def test_range(self):
        a = Tank("a")
        b = Tank("b")
        dispatches = [Dispatch(a, b, 50), Dispatch(a, b, 150), Dispatch(a, b, 200)]
        result = filter_dispatches_by_amount(dispatches, min_amount=100, max_amount=175)
        self.assertEqual(len(result), 1)


class TestDispatchesInvolving(unittest.TestCase):
    def test_as_source(self):
        a = Tank("a")
        b = Tank("b")
        c = Tank("c")
        dispatches = [Dispatch(b, a, 100), Dispatch(c, b, 50)]
        result = dispatches_involving(dispatches, "a")
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
