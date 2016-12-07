from Algorithms.LinkedLists.linked_list import LinkedList


def remove_dups(llist):

    occourences = {}
    runner = None

    for ele in llist:
        if ele.value not in occourences:
            occourences[ele.value] = 1
        else:
            runner.next = ele.next
        runner = ele

    return llist


def remove_dups_inplace(llist):

    runner = None

    for ele in llist:
        runner = ele
        search_ahead = ele.next
        while search_ahead:
            if search_ahead.value == ele.value:
                runner.next = search_ahead.next
            runner = search_ahead
            search_ahead = search_ahead.next

    return llist


def test_remove_dups():
    test_list = LinkedList([2, 2, 3, 3, 4])
    assert remove_dups(test_list) == LinkedList([2, 3, 4])
    test_list = LinkedList([2, 2, 3, 3, 4])
    assert remove_dups_inplace(test_list) == LinkedList([2, 3, 4])