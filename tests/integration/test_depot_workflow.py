"""Integration tests for complete depot workflows."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from depot import Depot


class TestBasicWorkflow(unittest.TestCase):
    def test_create_and_transfer(self):
        d = Depot()
        d.create_tank("supply", "standard")
        d.create_tank("demand", "standard")
        d.transfer("demand", "supply", 500)
        self.assertEqual(d.get_tank("demand").fuel_level, 500)
        self.assertEqual(d.get_tank("supply").fuel_level, -500)

    def test_multi_tank_chain(self):
        d = Depot()
        d.create_tank("a")
        d.create_tank("b")
        d.create_tank("c")
        d.transfer("b", "a", 100)
        d.transfer("c", "b", 60)
        self.assertEqual(d.get_tank("a").fuel_level, -100)
        self.assertEqual(d.get_tank("b").fuel_level, 40)
        self.assertEqual(d.get_tank("c").fuel_level, 60)

    def test_round_trip(self):
        d = Depot()
        d.create_tank("x")
        d.create_tank("y")
        d.transfer("y", "x", 200)
        d.transfer("x", "y", 200)
        self.assertEqual(d.get_tank("x").fuel_level, 0)
        self.assertEqual(d.get_tank("y").fuel_level, 0)
        self.assertEqual(len(d.log_entries()), 2)


class TestDispatchIntegrity(unittest.TestCase):
    def test_ids_sequential(self):
        d = Depot()
        d.create_tank("a")
        d.create_tank("b")
        for i in range(10):
            d.transfer("a", "b", 10)
        ids = [e.id for e in d.log_entries()]
        self.assertEqual(ids, list(range(1, 11)))

    def test_dispatch_references_correct_tanks(self):
        d = Depot()
        d.create_tank("src")
        d.create_tank("dst")
        dispatch = d.transfer("dst", "src", 100)
        self.assertIs(dispatch.dest_tank, d.get_tank("dst"))
        self.assertIs(dispatch.source_tank, d.get_tank("src"))

    def test_tank_dispatches_consistent(self):
        d = Depot()
        d.create_tank("a")
        d.create_tank("b")
        d.create_tank("c")
        d.transfer("b", "a", 100)
        d.transfer("c", "a", 50)
        d.transfer("c", "b", 30)
        a_dispatches = d.get_tank("a").dispatches()
        self.assertEqual(len(a_dispatches), 2)
        b_dispatches = d.get_tank("b").dispatches()
        self.assertEqual(len(b_dispatches), 2)
        c_dispatches = d.get_tank("c").dispatches()
        self.assertEqual(len(c_dispatches), 2)


class TestFuelConservation(unittest.TestCase):
    def test_total_fuel_zero(self):
        d = Depot()
        d.create_tank("a")
        d.create_tank("b")
        d.create_tank("c")
        d.transfer("b", "a", 100)
        d.transfer("c", "b", 50)
        d.transfer("a", "c", 25)
        total = sum(t.fuel_level for t in d.tanks())
        self.assertEqual(total, 0)

    def test_summary_matches_dispatches(self):
        d = Depot()
        d.create_tank("a")
        d.create_tank("b")
        d.transfer("a", "b", 100)
        d.transfer("b", "a", 30)
        total_in, total_out = d.fuel_summary()
        self.assertEqual(total_in, 130)
        expected = sum(e.amount for e in d.log_entries())
        self.assertEqual(total_in, expected)


if __name__ == "__main__":
    unittest.main()
