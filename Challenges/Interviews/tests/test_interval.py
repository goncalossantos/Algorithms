from unittest import TestCase

from Challenges.Interviews.merge_overlapping_intervals import Interval, InvalidInterval


class TestInterval(TestCase):
    STANDARD_INPUT = [1, 4]

    def test_init(self):
        test_invalid_cases = [
            None,
            [],
            [3, 2],
        ]

        for test in test_invalid_cases:
            with self.assertRaises(InvalidInterval):
                Interval(test)

        test_valid_cases = [
            [1, 2],
            [1, 1],
        ]
        for test in test_valid_cases:
            assert Interval(test).start == test[Interval.START_INDEX]
            assert Interval(test).end == test[Interval.END_INDEX]

    def test_start_getter(self):

        interval = Interval(self.STANDARD_INPUT)
        assert interval.start == interval._start

    def test_start_setter(self):

        interval = Interval(self.STANDARD_INPUT)
        assert interval.start == interval._start
        interval.start = 0
        assert interval.start == interval._start

    def test_end_getter(self):

        interval = Interval(self.STANDARD_INPUT)
        assert interval.end == interval._end

    def test_end_setter(self):

        interval = Interval(self.STANDARD_INPUT)
        assert interval.end == interval._end
        interval.start = 0
        assert interval.end == interval._end

    def test_overlap(self):
        interval = Interval(self.STANDARD_INPUT)
        test_valid_cases = [
            ([1, 2], True),
            ([1, 1], True),
            ([1, 3], True),
            ([1, 8], True),
            ([0, 8], True),
            ([0, 1], True),
            ([4, 5], True),
            ([5, 6], False),
        ]
        for test in test_valid_cases:
            assert interval.overlap(Interval(test[0])) == test[1]

    def test_merge(self):

        test_valid_cases = [
            ([1, 2], [1, 4]),
            ([1, 1], [1, 4]),
            ([1, 3], [1, 4]),
            ([1, 8], [1, 8]),
            ([0, 8], [0, 8]),
            ([0, 1], [0, 4]),
            ([4, 5], [1, 5]),
        ]
        for test in test_valid_cases:
            interval = Interval(self.STANDARD_INPUT)
            interval.merge(Interval(test[0]))
            assert interval.start == test[1][Interval.START_INDEX]
            assert interval.end == test[1][Interval.END_INDEX]
