from typing import List, Callable


def linear_search(sorted_numbers: List[int], target: int) -> int:
    """ Linearly searches a sorted array for a target

    :param sorted_numbers: input sorted numbers
    :param target: target value to search for
    :return: Returns the index where to place the the target value
        As this function is to be used with LIS, in the case of a <= target <= b, the index returned
        is the index of b
    """
    i = -1
    for i, n in enumerate(sorted_numbers):
        if n >= target:
            return i
    return i + 1


def lis_binary_search(sorted_numbers: List[int], target: int) -> int:
    """ binary search in a sorted array for a target

    :param sorted_numbers: input sorted numbers
    :param target: target value to search for
    :return: Returns the index where to place the the target value
        As this function is to be used with LIS, in the case of a <= target <= b, the index returned
        is the index of b
    """
    left = 0  # type: int
    right = len(sorted_numbers) - 1  # type: int

    if not sorted_numbers:
        return 0
    # if target is bigger than the entire input, return the end
    if target > sorted_numbers[right]:
        return right + 1
    while left <= right:
        mid = (right + left) // 2  # type: int

        if target > sorted_numbers[mid]:
            left = mid + 1
        elif target < sorted_numbers[mid]:
            right = mid - 1
        else:
            return mid

    return left


def insert_in_list(input_list: List[int], target: int, position: int) -> None:
    """ Inserts in the correct position in list of sorted numbers
    This function is to be used only with the lis algorithm in this file

    If the list is to small for position, append at the end

    :param input_list: sorted list of numbers
    :param target: target to be inserted
    :param position: where to insert
    """

    if position >= len(input_list):
        input_list.append(target)
    else:
        input_list[position] = target


def lis(numbers: List[int], search_func: Callable[[List[int], int], int]) -> int:
    """ Computes the longest increasing subsequence

    :param numbers: List of input numbers
    :param search_func: Function to be used to search where to insert the every number in the output list
    :return: Returns the length of the longest increasing subsequence
    """
    output_list = list()  # type: List[int]
    for n in numbers:
        insertion_index = search_func(sorted_numbers=output_list, target=n)
        insert_in_list(output_list, target=n, position=insertion_index)
    return len(output_list)
