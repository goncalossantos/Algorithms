import operator


def insertion_sort(array, reverse=False):

    lt = operator.lt if reverse else operator.gt
    for index in range(1, len(array)):

        currentvalue = array[index]
        position = index

        while position > 0 and lt(array[position - 1], currentvalue):
            array[position] = array[position - 1]
            position = position - 1

        array[position] = currentvalue

    return array


def reverse_insertion_sort(array):

    for index in range(1, len(array)):

        currentvalue = array[index]
        position = index

        while position > 0 and array[position - 1] < currentvalue:
            array[position] = array[position - 1]
            position = position - 1

        array[position] = currentvalue
    return array
