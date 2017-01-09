from typing import List, Union


class Fibonnaci(object):
    @staticmethod
    def recursive(n: int) -> int:

        if n == 0 or n == 1:
            return n
        return Fibonnaci.recursive(n - 1) + Fibonnaci.recursive(n - 2)

    @staticmethod
    def memoization(n: int, lookup: List[Union[int, None]]) -> int:

        # Base case
        if n == 0 or n == 1:
            lookup[n] = n

        # If the value is not calculated previously then calculate it
        if lookup[n] is None:
            lookup[n] = Fibonnaci.memoization(n - 1, lookup) + Fibonnaci.memoization(n - 2, lookup)

        # return the value corresponding to that value of n
        return lookup[n]

    @staticmethod
    def tabulation(n: int) -> int:

        prev = 0  # type: int
        result = 1  # type: int

        for i in range(2, n + 1):
            result, prev = result + prev, result
        return result
