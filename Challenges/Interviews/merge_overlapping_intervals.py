from typing import Sequence, List


class InvalidInterval(Exception):
    pass


class InvalidOperation(Exception):
    pass


class Interval(object):
    START_INDEX = 0
    END_INDEX = 1

    def __init__(self, input_ele: Sequence[int]) -> None:

        # Validate the interval
        if not input_ele or input_ele[self.START_INDEX] > input_ele[self.END_INDEX]:
            raise InvalidInterval("Invalid Input Arguments for Interval")

        self._start = input_ele[self.START_INDEX]
        self._end = input_ele[self.END_INDEX]

    @property
    def start(self) -> int:
        return self._start

    @start.setter
    def start(self, value: int) -> None:
        self._start = value

    @property
    def end(self) -> int:
        return self._end

    @end.setter
    def end(self, value: int) -> None:
        self._end = value

    def overlap(self, other: "Interval") -> bool:
        if Interval.is_valid_interval(other) is not True:
            raise InvalidOperation("Overlap method's other must be valid interval")
        return self._start <= other.start <= self._end or other.start <= self._start <= other.end

    def merge(self, other: "Interval") -> None:
        if Interval.is_valid_interval(other) is not True:
            raise InvalidOperation("Merge method's other must be valid interval")

        if self.overlap(other) is not True:
            raise InvalidOperation("Invalid Merge: Intervals do not overlap")
        self.start, self.end = min(self.start, other.start), max(self.end, other.end)

    @staticmethod
    def is_valid_interval(tentative):
        if not tentative or not hasattr(tentative, "start") or not hasattr(tentative, "end"):
            return False
        return True

    @classmethod
    def build_intervals(cls, input_list: Sequence[Sequence[int]]) -> List["Interval"]:
        return [cls(input_ele) for input_ele in input_list]

    def __str__(self) -> str:
        return "Interval({0},{1})".format(self.start, self.end)

    def __lt__(self, other):
        return self._start < other.start

    def serialize(self):
        return [self.start, self.end]


def merge_overlapping_intervals(input_list: Sequence[Sequence[int]]) -> List[Interval]:

    if not input_list:
        return []

    intervals = Interval.build_intervals(input_list)
    intervals.sort()

    to_merge = None
    output = []
    for interval in intervals:
        if not to_merge:
            # First object in the list
            to_merge = interval
            continue
        if to_merge.overlap(interval):
            to_merge.merge(interval)
        else:
            output.append(to_merge)
            to_merge = interval
    output.append(to_merge)

    return [interval.serialize() for interval in output]


def merge_quick_and_dirty(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,  # This is black magic
    return out
