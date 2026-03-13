"""Unit tests for the Dispatch and DispatchLog classes."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tank import Tank
from dispatch import Dispatch, DispatchLog


class TestDispatchCreation(unittest.TestCase):
    def test_create_dispatch(self):
        a = Tank("a")
        b = Tank("b")
        d = Dispatch(a, b, 100)
        self.assertEqual(d.id, 0)
        self.assertIs(d.dest_tank, a)
        self.assertIs(d.source_tank, b)
        self.assertEqual(d.amount, 100)
        self.assertEqual(d.note, "")

    def test_create_dispatch_with_note(self):
        a = Tank("a")
        b = Tank("b")
        d = Dispatch(a, b, 50, "test note")
        self.assertEqual(d.note, "test note")

    def test_id_setter(self):
        a = Tank("a")
        b = Tank("b")
        d = Dispatch(a, b, 10)
        d.id = 42
        self.assertEqual(d.id, 42)


class TestDispatchRepr(unittest.TestCase):
    def test_repr_format(self):
        a = Tank("alpha")
        b = Tank("beta")
        d = Dispatch(a, b, 200)
        d.id = 1
        expected = "Dispatch(id=1, dest='alpha', source='beta', amount=200)"
        self.assertEqual(repr(d), expected)


class TestDispatchLog(unittest.TestCase):
    def test_empty_log(self):
        log = DispatchLog()
        self.assertEqual(log.dispatches(), [])

    def test_record_assigns_id(self):
        log = DispatchLog()
        a = Tank("a")
        b = Tank("b")
        d = Dispatch(a, b, 100)
        log.record(d)
        self.assertEqual(d.id, 1)

    def test_record_sequential_ids(self):
        log = DispatchLog()
        a = Tank("a")
        b = Tank("b")
        d1 = Dispatch(a, b, 100)
        d2 = Dispatch(b, a, 50)
        log.record(d1)
        log.record(d2)
        self.assertEqual(d1.id, 1)
        self.assertEqual(d2.id, 2)

    def test_record_adds_to_both_tanks(self):
        log = DispatchLog()
        a = Tank("a")
        b = Tank("b")
        d = Dispatch(a, b, 100)
        log.record(d)
        self.assertEqual(len(a.dispatches()), 1)
        self.assertEqual(len(b.dispatches()), 1)

    def test_dispatches_returns_copy(self):
        log = DispatchLog()
        d1 = log.dispatches()
        d2 = log.dispatches()
        self.assertIsNot(d1, d2)

    def test_record_returns_dispatch(self):
        log = DispatchLog()
        a = Tank("a")
        b = Tank("b")
        d = Dispatch(a, b, 100)
        result = log.record(d)
        self.assertIs(result, d)


if __name__ == "__main__":
    unittest.main()
