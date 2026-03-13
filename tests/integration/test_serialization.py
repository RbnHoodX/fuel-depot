"""Integration tests for serialization round-trips."""

import sys
import os
import json
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from depot import Depot
from storage.serializer import depot_to_json, depot_to_dict, tank_to_dict, dispatch_to_dict
from storage.loader import load_json, validate_depot_data, extract_tank_names


class TestSerializationRoundTrip(unittest.TestCase):
    def setUp(self):
        self.depot = Depot()
        self.depot.create_tank("main")
        self.depot.create_tank("backup", "reserve")
        self.depot.transfer("main", "backup", 200)

    def test_to_dict_structure(self):
        data = depot_to_dict(self.depot)
        self.assertIn("tanks", data)
        self.assertIn("dispatches", data)
        self.assertEqual(len(data["tanks"]), 2)
        self.assertEqual(len(data["dispatches"]), 1)

    def test_json_round_trip(self):
        json_str = depot_to_json(self.depot)
        data = load_json(json_str)
        self.assertEqual(len(data["tanks"]), 2)
        names = extract_tank_names(data)
        self.assertIn("main", names)
        self.assertIn("backup", names)

    def test_validate_valid_data(self):
        data = depot_to_dict(self.depot)
        errors = validate_depot_data(data)
        self.assertEqual(errors, [])

    def test_validate_invalid_data(self):
        errors = validate_depot_data({})
        self.assertGreater(len(errors), 0)

    def test_tank_dict_has_fuel_level(self):
        tank = self.depot.get_tank("main")
        d = tank_to_dict(tank)
        self.assertEqual(d["fuel_level"], 200)

    def test_dispatch_dict_has_note(self):
        self.depot.transfer("backup", "main", 50, "return")
        dispatches = self.depot.log_entries()
        d = dispatch_to_dict(dispatches[-1])
        self.assertEqual(d["note"], "return")


if __name__ == "__main__":
    unittest.main()
