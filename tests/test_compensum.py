import unittest

from compensum import Sum
from sumsapi import Accumulator


class TestSum(unittest.TestCase):
    def test_add_counts(self):
        total = Sum()
        total.add(1.0)
        self.assertEqual(total.stats()["count"], 1)

    def test_total_accumulates(self):
        total = Sum()
        total.add(1.0)
        total.add(2.0)
        self.assertEqual(total.stats()["total"], 3.0)

    def test_empty_total(self):
        self.assertEqual(Sum().stats()["total"], 0.0)

    def test_stats_shape(self):
        self.assertIn("compensated", Sum().stats())

    def test_accumulator_wraps(self):
        accumulator = Accumulator()
        accumulator.add(1.0)
        self.assertEqual(accumulator.sum.stats()["count"], 1)


if __name__ == "__main__":
    unittest.main()
