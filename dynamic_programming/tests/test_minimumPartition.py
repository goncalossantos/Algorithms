from unittest import TestCase

from dynamic_programming.minimum_partition import MinimumPartition, MinSet


class TestMinimumPartition(TestCase):
    def test_recursive(self):
        out = MinimumPartition.recursive([3, 1, 4, 2, 2, 1], MinSet(), MinSet())
        assert out == 1
