from unittest import TestCase

from dynamic_programming.fibonnaci import Fibonnaci


class TestFibonnaci(TestCase):
    TEST_CASES = [
        (5, 5),
        (10, 55),
        (50, 12586269025),
        (100, 354224848179261915075),
    ]

    def test_recursive(self):
        for test_case in self.TEST_CASES[:2]:
            assert Fibonnaci.recursive(test_case[0]) == test_case[1]

    def test_memoization(self):
        for test_case in self.TEST_CASES:
            l = [None] * (test_case[0] + 1)
            assert Fibonnaci.memoization(test_case[0], l) == test_case[1]

    def test_tabulation(self):
        for test_case in self.TEST_CASES:
            assert Fibonnaci.tabulation(test_case[0]) == test_case[1]
