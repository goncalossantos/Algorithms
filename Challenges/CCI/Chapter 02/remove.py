from Algorithms.LinkedLists.linked_list import LinkedList


def remove(node):

    if node.next:
        node.value = node.next.value
        node.next = node.next.next
    else:
        # Node at the end of the list
        raise Exception("Node not in the middle")


def test_remove():
    test_list = LinkedList([1, 2, 3, 4, 5])
    middle_node = test_list.append(6)
    test_list.add_multiple([7, 8, 9])

    expected = LinkedList([1, 2, 3, 4, 5, 7, 8, 9])

    remove(middle_node)
    assert test_list == expected
