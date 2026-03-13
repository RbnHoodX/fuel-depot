"""Unit tests for the Tank class."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tank import Tank
from dispatch import Dispatch


class TestTankCreation(unittest.TestCase):
    def test_create_default_kind(self):
        t = Tank("alpha")
        self.assertEqual(t.name, "alpha")
        self.assertEqual(t.kind, "standard")

    def test_create_reserve_kind(self):
        t = Tank("bravo", "reserve")
        self.assertEqual(t.kind, "reserve")

    def test_initial_fuel_level_zero(self):
        t = Tank("charlie")
        self.assertEqual(t.fuel_level, 0)

    def test_initial_dispatches_empty(self):
        t = Tank("delta")
        self.assertEqual(t.dispatches(), [])


class TestTankFuelLevel(unittest.TestCase):
    def test_fuel_level_after_receiving(self):
        dest = Tank("dest")
        src = Tank("src")
        d = Dispatch(dest, src, 100)
        dest._add_dispatch(d)
        src._add_dispatch(d)
        self.assertEqual(dest.fuel_level, 100)

    def test_fuel_level_after_sending(self):
        dest = Tank("dest")
        src = Tank("src")
        d = Dispatch(dest, src, 50)
        dest._add_dispatch(d)
        src._add_dispatch(d)
        self.assertEqual(src.fuel_level, -50)

    def test_fuel_level_multiple_dispatches(self):
        a = Tank("a")
        b = Tank("b")
        d1 = Dispatch(a, b, 200)
        d2 = Dispatch(b, a, 80)
        a._add_dispatch(d1)
        b._add_dispatch(d1)
        a._add_dispatch(d2)
        b._add_dispatch(d2)
        self.assertEqual(a.fuel_level, 120)
        self.assertEqual(b.fuel_level, -120)

    def test_fuel_level_is_computed_not_stored(self):
        t = Tank("test")
        self.assertFalse(hasattr(t, "_fuel_level"))


class TestTankRepr(unittest.TestCase):
    def test_repr_format(self):
        t = Tank("main", "standard")
        self.assertEqual(repr(t), "Tank(name='main', kind='standard')")

    def test_repr_reserve(self):
        t = Tank("backup", "reserve")
        self.assertEqual(repr(t), "Tank(name='backup', kind='reserve')")


class TestTankDispatches(unittest.TestCase):
    def test_dispatches_returns_copy(self):
        t = Tank("test")
        d1 = t.dispatches()
        d2 = t.dispatches()
        self.assertIsNot(d1, d2)

    def test_dispatch_recorded(self):
        a = Tank("a")
        b = Tank("b")
        d = Dispatch(a, b, 10)
        a._add_dispatch(d)
        self.assertEqual(len(a.dispatches()), 1)


if __name__ == "__main__":
    unittest.main()
