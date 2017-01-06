import heapq
from itertools import count

from typing import List, Any, Dict, TypeVar, Generic, Union

T = TypeVar("T")


# TODO: Add support for Any type items instead of just int (right now they have to be the indexes)


class PriorityQueue(Generic[T]):
    """ Implements a priority queue using heapq

        Has the functionality to push, pop, heapify update and pop_all from heap
        To build a a new object from a queue use the ''@classmethod PriorityQueue.build()''
    """

    REMOVED = '<removed-task>'  # placeholder for a removed task

    def __init__(self):
        self.access_counter = count()
        self._queue = list()  # type: List[T]
        self.entry_finder = dict()  # type: Dict[T]

    def __len__(self):
        return len(self.entry_finder)

    def push(self, item: Any, priority: int = 0) -> None:
        """ Pushes/updates an item into/in the priority queue

        :param item: What will be the added to the priority queue
        :param priority: the item's priority
        """

        # Create the entry and update entry_finder
        entry = self.entry_handler(item, priority)
        # Add to heap
        heapq.heappush(self._queue, entry)

    def entry_handler(self, item: Any, priority: int = 0) -> List[Any]:
        """ Creates the entry that will be stored on the heap
`
        This function handles all the challenges in a good implementation of priority queue
        1 - Sort stability: how do you get two tasks with equal priorities to be returned in the order
        they were originally added?
        2 - Tuple comparison breaks for (priority, task) pairs if the priorities are equal and the tasks do
        not have a default comparison order. If the priority of a task changes, how do you move it to a new position
        in the heap? Or if a pending task needs to be deleted, how do you find it and remove it from the queue?

        The solution for these two challenges is the addition of a counter

        3 - If the priority of a task changes, how do you move it to a new position in the heap?
        4 - Or if a pending task needs to be deleted, how do you find it and remove it from the queue?

        The solution for these challenges is to keep an entry_finder dictionary that points to the entry in the
        priority queue

        :param item: What will be the added to the priority queue
        :param priority: the item's priority
        :return: Returns the entry object: ``entry = [priority, count, item]``, type: ``List[int, Dict, Any ]``
        """
        # Remove item from entry finder if it is there and mark the entry with the ''REMOVED'' flag
        if item in self.entry_finder:
            self.remove_task(item)
        # Update access counter
        access_counter = next(self.access_counter)
        # Add item to entry_finder and heap

        entry = [-priority, access_counter, item]  # Minus because we want a min heap
        self.entry_finder[item] = entry
        return entry

    def heapify(self, input_elements: List[Union[int, float]]):
        """ Implements a heapify functionality for the priority queue

        The reason why ``heapq.heapify`` can't be performed directly in input_elements is that we need to create and
        handle a new entry for every element in the input list


        .. seealso:: ''PriorityQueue.entry_handler''
        .. TODO:: Add support for Any type items instead of just int (right now they have to be the indexes)

        :param input_elements: List of either int of float priorities.
        :return:
        """
        entry_list = list()
        for i, priority in enumerate(input_elements):
            entry_list.append(self.entry_handler(i, priority=priority))
        heapq.heapify(entry_list)
        self._queue = entry_list

    def remove_task(self, item: Any) -> None:
        """ Mark an existing task as REMOVED.

        Raise KeyError if not found.

        :param item: Item to remove
        """
        entry = self.entry_finder.pop(item)
        entry[-1] = self.REMOVED

    def pop(self):
        """ Pops an item from the priority queue

        This method continually pops elements until it finds one that doesn't have the ''REMOVED'' flag set
        Raise KeyError if key becomes empty before a valid item can be returned

        :return:
        """
        while self._queue:
            priority, access_counter, item = heapq.heappop(self._queue)
            if item is not self.REMOVED:
                del self.entry_finder[item]
                return item
        raise KeyError('pop from an empty priority queue')

    @classmethod
    def build(cls, input_elements: List[Any]) -> 'PriorityQueue':
        """ Builds the priority queue from an input by calling heapify

        :param input_elements:
        :return: Returns the new PriorityQueue object
        """

        new_queue = PriorityQueue()
        new_queue.heapify(input_elements)
        return new_queue

    def pop_all(self) -> List[Any]:
        """ Pops all valid elements from queue

        :return: Returns a 'list()' object with all the elements
        """
        output = list()
        while self._queue:
            output.append(self.pop())
        print(output)
        return output

    def contains_item(self, item):
        return item in self.entry_finder


def test_build():
    l = [2, 1, 10, 4, 5]
    pq = PriorityQueue.build(l)
    assert pq.pop_all() == [1, 0, 3, 4, 2][::-1]


test_build()
