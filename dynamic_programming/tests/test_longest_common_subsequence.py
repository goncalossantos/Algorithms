from unittest import TestCase

from dynamic_programming.longest_common_subsequence import lcs


class TestLCS(TestCase):
    TEST_CASES = [
        ("", "", 0),
        ("", "A", 0),
        ("A", "", 0),
        ("A", "A", 1),
        ("A", "B", 0),
        ("ABCD", "AEDF", 2),
        ("ABCD", "AD", 2),
        ("AD", "ABD", 2),
        ("ADTRYUIO", "ABDHJKTRYEUIO", 8),
    ]

    def test_lcs(self):
        for test_case in self.TEST_CASES:
            assert lcs(test_case[0], test_case[1]) == test_case[2]
