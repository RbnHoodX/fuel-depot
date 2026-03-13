"""Integration tests for report generation."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from depot import Depot
from reports.generator import (
    tank_status_report,
    dispatch_summary_report,
    top_receivers,
    top_senders,
    idle_tanks,
)
from reports.statistics import dispatch_amount_stats, fuel_level_distribution
from reports.formatter import format_tank_row, format_dispatch_row, format_summary


class TestReportGeneration(unittest.TestCase):
    def setUp(self):
        self.depot = Depot()
        self.depot.create_tank("a")
        self.depot.create_tank("b")
        self.depot.create_tank("c")
        self.depot.transfer("b", "a", 200)
        self.depot.transfer("c", "a", 100)
        self.depot.transfer("c", "b", 50)

    def test_tank_status_report(self):
        report = tank_status_report(self.depot.tanks())
        self.assertEqual(len(report), 3)
        a_report = next(r for r in report if r["name"] == "a")
        self.assertEqual(a_report["fuel_level"], -300)

    def test_dispatch_summary(self):
        summary = dispatch_summary_report(self.depot.log_entries())
        self.assertEqual(summary[("a", "b")], 200)
        self.assertEqual(summary[("a", "c")], 100)

    def test_top_receivers(self):
        top = top_receivers(self.depot.log_entries(), limit=2)
        self.assertEqual(top[0][0], "b")
        self.assertEqual(top[0][1], 200)

    def test_top_senders(self):
        top = top_senders(self.depot.log_entries())
        self.assertEqual(top[0][0], "a")
        self.assertEqual(top[0][1], 300)

    def test_idle_tanks(self):
        self.depot.create_tank("idle")
        result = idle_tanks(self.depot.tanks())
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "idle")


class TestStatisticsIntegration(unittest.TestCase):
    def test_dispatch_stats(self):
        depot = Depot()
        depot.create_tank("a")
        depot.create_tank("b")
        depot.transfer("a", "b", 100)
        depot.transfer("a", "b", 200)
        depot.transfer("a", "b", 300)
        stats = dispatch_amount_stats(depot.log_entries())
        self.assertEqual(stats["count"], 3)
        self.assertEqual(stats["mean"], 200.0)

    def test_fuel_distribution(self):
        depot = Depot()
        depot.create_tank("a")
        depot.create_tank("b")
        depot.transfer("a", "b", 100)
        dist = fuel_level_distribution(depot.tanks())
        self.assertEqual(dist["count"], 2)
        self.assertEqual(dist["total"], 0)


class TestFormatterIntegration(unittest.TestCase):
    def test_format_tank_row(self):
        row = format_tank_row("main", 500.0, "standard")
        self.assertIn("main", row)
        self.assertIn("500.00", row)

    def test_format_dispatch_row(self):
        row = format_dispatch_row(1, "a", "b", 100, "test")
        self.assertIn("a", row)
        self.assertIn("b", row)
        self.assertIn("test", row)

    def test_format_summary(self):
        summary = format_summary(1000, 800, 5)
        self.assertIn("1000.00", summary)
        self.assertIn("5", summary)


if __name__ == "__main__":
    unittest.main()
