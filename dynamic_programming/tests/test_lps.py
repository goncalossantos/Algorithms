from unittest import TestCase

from dynamic_programming.longest_palindrome_subsequence import lps


class TestLps(TestCase):
    def test_lps(self):
        assert lps("character") == "carac"
        assert lps("abcdbfga") == "abcba"
