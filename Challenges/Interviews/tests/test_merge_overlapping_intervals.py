from unittest import TestCase

from Challenges.Interviews.merge_overlapping_intervals import merge_overlapping_intervals


class TestMerge_overlapping_intervals(TestCase):
    def test_merge_overlapping_intervals(self):
        test = [
            [1, 4],
            [2, 5],
            [6, 7],
            [7, 8],
        ]
        result = [
            [1, 5],
            [6, 8]
        ]
        print(merge_overlapping_intervals(test))
        assert merge_overlapping_intervals(test) == result
