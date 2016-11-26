import operator


def insertion_sort(array, reverse=False):

    lt = operator.lt if not reverse else operator.gt
    for index in range(1, len(array)):

        currentvalue = array[index]
        position = index

        while position > 0 and lt(currentvalue, array[position - 1]):
            array[position] = array[position - 1]
            position = position - 1

        array[position] = currentvalue

    return array
# TODO: Improve memory usage (how in python?) and do a non recursive version

# O(n*log(n))


def merge_sort(array, reverse=False):

    lt = operator.lt if not reverse else operator.gt

    def merge(array_merge, L, R):
        i = 0
        j = 0
        # Add infinity to end (sentinel)
        L.append(float("inf"))
        R.append(float("inf"))
        for k in range(len(array_merge)):

            if lt(L[i], R[j]):
                array_merge[k] = L[i]
                i += 1
            else:
                array_merge[k] = R[j]
                j += 1
        return array_merge

    if len(array) > 1:

        q = len(array) / 2
        A1 = merge_sort(array[:q])
        A2 = merge_sort(array[q:])
        array = merge(array, A1, A2)

    return array
