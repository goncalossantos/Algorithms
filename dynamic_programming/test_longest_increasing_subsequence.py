from collections import namedtuple
from unittest import TestCase

from dynamic_programming.longest_inc_subsequence import lis, linear_search, lis_binary_search, insert_in_list


class TestLis(TestCase):
    TEST_CASES = [
        ([10, 22, 9, 33, 21, 50, 41, 60, 80], 6),
        ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6)
    ]

    def test_lis(self):
        for test_case in self.TEST_CASES:
            assert test_case[1] == lis(test_case[0], linear_search)
            assert test_case[1] == lis(test_case[0], lis_binary_search)


class TestSearchSorted(TestCase):
    SearchTest = namedtuple("SearchTest", ["input", "target", "output_pos", "output"])
    TEST_CASES = [
        SearchTest([], 3, 0, [3]),
        SearchTest([3], 1, 0, [1]),
        SearchTest([1], 3, 1, [1, 3]),
        SearchTest([1, 2, 4, 5], 3, 2, [1, 2, 3, 5]),
        SearchTest([1, 2, 4, 5], 1, 0, [1, 2, 4, 5]),
        SearchTest([0, 2, 4, 5], 0, 0, [0, 2, 4, 5]),
        SearchTest([0, 2, 4, 5], 5, 3, [0, 2, 4, 5]),
        SearchTest([0, 1, 2, 4, 5], 2, 2, [0, 1, 2, 4, 5]),
        SearchTest([0, 1, 2, 4, 5], 1, 1, [0, 1, 2, 4, 5]),
        SearchTest([0, 1, 2, 4, 5], 3, 3, [0, 1, 2, 3, 5]),
        SearchTest([0, 2, 4, 5], 6, 4, [0, 2, 4, 5, 6]),
    ]

    def test_linear_search(self):
        for test_case in self.TEST_CASES:
            assert linear_search(test_case.input, test_case.target) == test_case.output_pos

    def test_lis_binary_search(self):
        for test_case in self.TEST_CASES:
            assert lis_binary_search(test_case.input, test_case.target) == test_case.output_pos

    def test_search_and_place(self):
        for test_case in self.TEST_CASES:
            insert_in_list(test_case.input, test_case.target, test_case.output_pos)
            assert test_case.input == test_case.output
