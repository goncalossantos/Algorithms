# Introduction to Algorithms, Third edition, Chapter 4.1


def maximum_cross_subarray(a, left, right, mid):
    """Gets the maximum sum continuous cross subarray

    Returns the continuous subarray with the greatest sum
    with the constraint that that subarray must cross the
    midpoint.

    Arguments:
        a {array of ints} -- Full Array
        left {int} -- left index of subarray
        right {int} -- right index of subarray
        mid {int} -- mid point of the subarray
    Return:
        tuple -> (left_index, right_index, max_sum)
    """
    max_left = 0
    max_right = 0
    sum_left = 0
    sum_right = 0

    sum = 0
    for i in range(mid, left - 1, -1):
        sum += a[i]
        if sum >= sum_left:
            sum_left = sum
            max_left = i

    sum = 0
    for i in range(mid + 1, right + 1, 1):
        sum += a[i]
        if sum >= sum_right:
            sum_right = sum
            max_right = i

    return (max_left, max_right, sum_left + sum_right)


def maximum_subarray(array, l, r):
    """Calculates maximum subarray of array

    By using recursion on an array, returns the
    coninuous subarray that has the maximum sum

    Arguments:
        array {[type]} -- [description]
        l {[type]} -- [description]
        r {[type]} -- [description]
    """

    if r == l:
        # Only one element in subarray, return
        return (l, r, array[r])

    q = (r + l) / 2

    left_left, left_right, left_sum = maximum_subarray(array, l, q)
    right_left, right_right, right_sum = maximum_subarray(array, q + 1, r)
    cross_left, cross_right, cross_sum = maximum_cross_subarray(array, l, r, q)

    # Return the indexes correspoding to the maximum sum
    # between left, right and cross
    indexes = [
        (left_left, left_right), (right_left, right_right),
        (cross_left, cross_right)
    ]
    sums = [left_sum, right_sum, cross_sum]
    index = sums.index(max(sums))
    return (indexes[index][0], indexes[index][1], max(sums))
