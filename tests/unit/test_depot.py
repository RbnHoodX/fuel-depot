"""Unit tests for the Depot class."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from depot import Depot


class TestDepotCreation(unittest.TestCase):
    def test_empty_depot(self):
        d = Depot()
        self.assertEqual(d.tanks(), [])
        self.assertEqual(d.log_entries(), [])

    def test_create_tank(self):
        d = Depot()
        t = d.create_tank("main")
        self.assertEqual(t.name, "main")
        self.assertEqual(t.kind, "standard")

    def test_create_tank_reserve(self):
        d = Depot()
        t = d.create_tank("backup", "reserve")
        self.assertEqual(t.kind, "reserve")

    def test_duplicate_tank_raises(self):
        d = Depot()
        d.create_tank("main")
        with self.assertRaises(ValueError):
            d.create_tank("main")

    def test_get_tank(self):
        d = Depot()
        d.create_tank("main")
        t = d.get_tank("main")
        self.assertEqual(t.name, "main")

    def test_get_tank_missing_raises(self):
        d = Depot()
        with self.assertRaises(KeyError):
            d.get_tank("missing")


class TestDepotTransfer(unittest.TestCase):
    def test_basic_transfer(self):
        d = Depot()
        d.create_tank("a")
        d.create_tank("b")
        dispatch = d.transfer("a", "b", 100)
        self.assertEqual(dispatch.amount, 100)

    def test_transfer_updates_fuel_levels(self):
        d = Depot()
        d.create_tank("a")
        d.create_tank("b")
        d.transfer("a", "b", 100)
        self.assertEqual(d.get_tank("a").fuel_level, 100)
        self.assertEqual(d.get_tank("b").fuel_level, -100)

    def test_transfer_zero_raises(self):
        d = Depot()
        d.create_tank("a")
        d.create_tank("b")
        with self.assertRaises(ValueError):
            d.transfer("a", "b", 0)

    def test_transfer_negative_raises(self):
        d = Depot()
        d.create_tank("a")
        d.create_tank("b")
        with self.assertRaises(ValueError):
            d.transfer("a", "b", -10)

    def test_transfer_missing_tank_raises(self):
        d = Depot()
        d.create_tank("a")
        with self.assertRaises(KeyError):
            d.transfer("a", "missing", 100)

    def test_transfer_with_note(self):
        d = Depot()
        d.create_tank("a")
        d.create_tank("b")
        dispatch = d.transfer("a", "b", 50, "test")
        self.assertEqual(dispatch.note, "test")


class TestDepotLogAndSummary(unittest.TestCase):
    def test_log_entries(self):
        d = Depot()
        d.create_tank("a")
        d.create_tank("b")
        d.transfer("a", "b", 100)
        d.transfer("b", "a", 50)
        self.assertEqual(len(d.log_entries()), 2)

    def test_fuel_summary(self):
        d = Depot()
        d.create_tank("a")
        d.create_tank("b")
        d.transfer("a", "b", 100)
        d.transfer("b", "a", 50)
        total_in, total_out = d.fuel_summary()
        self.assertEqual(total_in, 150)
        self.assertEqual(total_out, 150)

    def test_tanks_returns_list(self):
        d = Depot()
        d.create_tank("a")
        d.create_tank("b")
        tanks = d.tanks()
        self.assertIsInstance(tanks, list)
        self.assertEqual(len(tanks), 2)


if __name__ == "__main__":
    unittest.main()
