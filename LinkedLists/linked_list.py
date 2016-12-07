class InvalidOperation(Exception):
    pass


class Node(object):
    """Node of a linked list

    Represents a noded of a linked list
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return (str(self.value), self.next is not None)


class LinkedList(object):
    """Node of a linked list

    Represents a noded of a linked list
    """

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def append(self, value):

        pointer = self.head
        new_node = Node(value)

        if not pointer:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        return self.tail

    def push(self, value):

        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

    def insert(self, value, pos):

        counter = 0
        pointer = self.head
        if not pointer:
            raise InvalidOperation("List is Empty")

        while pointer and counter < pos:
            pointer = pointer.next
            counter += 1

        new_node = Node(value, next=pointer.next)
        pointer.next = new_node

    def delete(self, pos):

        counter = 0
        pointer = self.head
        if not pointer:
            raise InvalidOperation("List is Empty")

        while pointer.next is not None and counter < (pos - 1):
            pointer = pointer.next
            counter += 1

        if not pointer.next:
            raise InvalidOperation(
                "Delete from position {} impossible,"
                " list only has {} nodes".format(pos, counter))

        aux = pointer.next
        pointer.next = pointer.next.next
        del aux

    def get(self, pos):

        pointer = self.head
        counter = 0
        if not pointer:
            raise InvalidOperation("Invalid Get() operation - Empty List")
        else:
            while pointer and counter < pos:
                pointer = pointer.next
                counter += 1
            return pointer.value

    def add_multiple(self, values):
        for v in values:

            self.append(v)

    def as_list(self):
        return [n.value for n in self]

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.as_list() == other.as_list()
        return False

    def __ne__(self, other):
        """Define a non-equality test"""
        return not self.__eq__(other)

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.value == item:
                found = True
            else:
                current = current.next

        return found


print LinkedList([1,2,3,4,5,6,7,8])
