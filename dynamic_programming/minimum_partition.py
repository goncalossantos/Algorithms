from typing import List, Tuple


class MinSet(list):
    """ Minimum set class extends the builtin set class to also maintain a total of the elements in it
    """

    def __init__(self) -> None:
        self.total = 0  # type: int
        super(MinSet, self).__init__()

    def append(self, value: int) -> None:
        """
        Adds to the set and to self.total

        :param value: value to add to the set
        """
        self.total += value
        super(MinSet, self).append(value)


class MinimumPartition(object):
    @classmethod
    def recursive(cls, numbers: List, min_set_a: MinSet, min_set_b: MinSet) -> Tuple[MinSet, MinSet]:

        if not numbers:
            return min_set_a, min_set_b

        to_consider = numbers.pop()
        min_set_a.append(to_consider)
        a_tentative_a, a_tentative_b = cls.recursive(numbers, min_set_a, min_set_b)
        min_set_a.remove(to_consider)
        min_set_a.total -= to_consider

        min_set_b.append(to_consider)
        b_tentative_a, b_tentative_b = cls.recursive(numbers, min_set_a, min_set_b)
        min_set_b.remove(to_consider)
        min_set_a.total -= to_consider

        if abs(a_tentative_a.total - a_tentative_b.total) < abs(b_tentative_a.total - b_tentative_b.total):
            min_set_a.append(to_consider)
            return a_tentative_a, a_tentative_b
        else:
            min_set_b.append(to_consider)
            return b_tentative_a, b_tentative_a
