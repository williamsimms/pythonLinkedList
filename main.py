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

        self.head = self.head.next


    def remove_last(self):
        if not self.head:
            return


list = LinkedList()
list.insert_first(22)
list.insert_first(26)
list.insert_first(76)
print(list.get_last())
