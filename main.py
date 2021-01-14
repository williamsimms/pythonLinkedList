class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str({'data': self.data, 'next': self.next})

    def __str__(self):
        return str({'data': self.data, 'next': self.next})


class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    def __repr__(self):
        return str(self.head)

    def insert_first(self, data):
        self.head = Node(data, self.head)

    def length(self):
        if not self.head:
            return

        node = self.head
        counter = 0

        while node:
            node = node.next
            counter += 1

        return counter

    def get_first(self):
        if not self.head:
            return

        return self.head

    def get_last(self):
        if not self.head:
            return

        node = self.head

        while node:
            if node.next == None:
                return node

            node = node.next

        return node

    def clear(self):
        self.head = None

    def remove_first(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        self.head = self.head.next

    def remove_last(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        previous = self.head
        node = self.head.next

        while node.next:
            previous = node
            node = node.next

        previous.next = None

    def insert_last(self, data):
        if not self.head:
            self.head = Node(data)
            return

        last = self.get_last()

        last.next = Node(data)

    def get_at(self, index):
        if not self.head:
            return

        counter = 0
        node = self.head

        while node:
            if index == counter:
                return node

            node = node.next
            counter += 1

        return None

    def insert_at(self, index, data):
        if not self.head:
            self.head = Node(data)
            return

        if index == 0:
            self.head = Node(data, self.head)
            return

        previous_node = self.get_at(index - 1)
        node = Node(data, previous_node.next)
        previous_node.next = node

    def remove_at(self, index):
        if not self.head:
            return

        if (index == 0):
            self.head = self.head.next
            return

        previous = self.get_at(index - 1)

        if not previous or not previous.next:
            return

        previous.next = previous.next.next

    def reverse(self):
        if not self.head:
            return

        previous = None
        current = self.head
        next = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous

    def for_each(self, fn):
        if not self.head:
            return

        node = self.head
        counter = 0

        while node:
            new_data = fn(node.data, counter)
            node.data = new_data
            node = node.next
            counter += 1


list = LinkedList()
list.insert_first(22)
list.insert_first(26)
list.insert_first(76)
print(list.get_last())
list.remove_last()
print(list.get_last())
list.insert_first(56)
list.insert_last(101)
print(list.get_last())
print(list.get_first())
list.reverse()
print(list.get_first())
list.for_each(lambda num, index: num * 2)
print(list.get_first())
