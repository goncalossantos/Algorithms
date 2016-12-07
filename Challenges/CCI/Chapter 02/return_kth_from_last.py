from Algorithms.LinkedLists.linked_list import LinkedList


def kth_from_last(l, k):

    runner = current = l.head

    index = 0
    while runner and index < k:
        runner = runner.next
        index += 1

    if not runner:
        raise Exception("List is not long enough")

    while runner:
        runner = runner.next
        current = current.next

    return current.value


def test_kth_from_last():
    test_list = LinkedList([1, 2, 3, 4, 5])
    assert kth_from_last(test_list, 3) == 3
    assert kth_from_last(test_list, 4) == 2
