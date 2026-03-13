"""Unit tests for formula modules."""

import sys
import os
import math
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from formulas.flow import flow_rate, pressure_drop, reynolds_number, volume_from_cylinder, fill_time
from formulas.pressure import hydrostatic_pressure, gauge_to_absolute, tank_bottom_pressure
from formulas.efficiency import transfer_efficiency, evaporation_loss, pipeline_loss, net_delivery


class TestFlowRate(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(flow_rate(100, 10), 10.0)

    def test_zero_duration_raises(self):
        with self.assertRaises(ValueError):
            flow_rate(100, 0)


class TestPressureDrop(unittest.TestCase):
    def test_basic(self):
        result = pressure_drop(100, 0.1, 2.0)
        self.assertGreater(result, 0)

    def test_zero_diameter_raises(self):
        with self.assertRaises(ValueError):
            pressure_drop(100, 0, 2.0)


class TestReynoldsNumber(unittest.TestCase):
    def test_basic(self):
        re = reynolds_number(2.0, 0.1)
        self.assertGreater(re, 0)


class TestVolumeFromCylinder(unittest.TestCase):
    def test_basic(self):
        v = volume_from_cylinder(1, 1)
        self.assertAlmostEqual(v, math.pi)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            volume_from_cylinder(-1, 1)


class TestFillTime(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(fill_time(100, 10), 10.0)


class TestHydrostaticPressure(unittest.TestCase):
    def test_basic(self):
        p = hydrostatic_pressure(1000, 10)
        self.assertAlmostEqual(p, 98100)


class TestGaugeToAbsolute(unittest.TestCase):
    def test_default(self):
        self.assertEqual(gauge_to_absolute(0), 101325)


class TestTransferEfficiency(unittest.TestCase):
    def test_perfect(self):
        self.assertEqual(transfer_efficiency(100, 100), 100.0)

    def test_partial(self):
        self.assertEqual(transfer_efficiency(90, 100), 90.0)

    def test_zero_dispatched_raises(self):
        with self.assertRaises(ValueError):
            transfer_efficiency(90, 0)


class TestEvaporationLoss(unittest.TestCase):
    def test_basic(self):
        loss = evaporation_loss(1000, 30, 24)
        self.assertGreater(loss, 0)


class TestPipelineLoss(unittest.TestCase):
    def test_basic(self):
        loss = pipeline_loss(1000, 50)
        self.assertEqual(loss, 100.0)


class TestNetDelivery(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(net_delivery(100, 10), 90)

    def test_clamps_to_zero(self):
        self.assertEqual(net_delivery(10, 100), 0)


if __name__ == "__main__":
    unittest.main()
