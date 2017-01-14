from unittest import TestCase

from dynamic_programming.edit_distance import EditDistance


class TestEditDistance(TestCase):
    TEST_CASES = [
        ("sunday", "saturday", 3),
    ]

    def test_recursive(self):
        for test_case in self.TEST_CASES:
            result = EditDistance.recursive(test_case[0], test_case[1])
            assert result == test_case[2]

    def test_tabulation(self):
        for test_case in self.TEST_CASES:
            assert EditDistance.tabulation(test_case[0], test_case[1]) == test_case[2]
