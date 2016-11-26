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


def recursive_maximum_subarray(array, l, r):
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
        return (l, r, array[l])

    q = (r + l) / 2

    left_left, left_right, left_sum = recursive_maximum_subarray(array, l, q)
    right_left, right_right, right_sum = recursive_maximum_subarray(array,
                                                                    q + 1, r)
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


def maximum_subarray(array, l, r):

    max_left = l
    best_so_far = best_now = array[l]
    now = array[l]
    tentative_left = l
    for i in range(l + 1, r + 1):
        best_now  = max(best_now + array[i], array[i])
        if best_now == array[i]:
            tentative_left = i
        tentative_best_so_far = max(best_so_far, best_now)
        if tentative_best_so_far == best_now:
            max_left = tentative_left
            max_right = i
            best_so_far = tentative_best_so_far

    return (max_left, max_right, best_so_far)


def maximum_subarray_sum(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def maximum_subarray_sum_2(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

print maximum_subarray([5,5,-11,9,20], 0, len([5,5,-9,10,20])-1)
print recursive_maximum_subarray([5,5,-11,9,20], 0, len([5,5,-9,10,20])-1)
print maximum_subarray_sum([5,5,-11,9,20])


