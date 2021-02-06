class Node:

    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return str({'data': self.data, 'next': self.next})

    def __str__(self) -> str:
        return str({'data': self.data, 'next': self.next})


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        linked_list = ''

        if not self.head:
            return None

        current = self.head

        while current:
            linked_list += str(current.data)
            linked_list += ' -> '
            current = current.next

        linked_list += 'None'
        return linked_list

    def print(self) -> str:
        return str(self.head)

    def __repr__(self) -> str:
        return str(self.head)

    def insert_first(self, data) -> None:
        self.head = Node(data, self.head)

    def length(self) -> int:
        if not self.head:
            return 0

        node = self.head
        counter = 0

        while node:
            node = node.next
            counter += 1

        return counter

    def __len__(self) -> int:
        return self.length()

    def get_first(self) -> Node:
        if not self.head:
            return

        return self.head

    def get_last(self) -> Node:
        if not self.head:
            return

        node = self.head

        while node:
            if node.next == None:
                return node

            node = node.next

        return node

    def clear(self) -> None:
        self.head = None

    def remove_first(self) -> None:
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        self.head = self.head.next

    def remove_last(self) -> None:
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

    def insert_last(self, data) -> None:
        if not self.head:
            self.head = Node(data)
            return

        last = self.get_last()

        last.next = Node(data)

    def get_at(self, index) -> Node or None:
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

    def __getitem__(self, index: int) -> Node or None:
        if type(index) != int:
            return

        return self.get_at(index)

    def insert_at(self, index: int, data) -> None:
        if not self.head:
            self.head = Node(data)
            return

        if index == 0:
            self.head = Node(data, self.head)
            return

        previous_node = self.get_at(index - 1) or self.get_last()
        node = Node(data, previous_node.next)
        previous_node.next = node

    def remove_at(self, index: int) -> None:
        if not self.head:
            return

        if (index == 0):
            self.head = self.head.next
            return

        previous = self.get_at(index - 1)

        if not previous or not previous.next:
            return

        previous.next = previous.next.next

    def reverse(self) -> None:
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

    def for_each(self, fn) -> None:
        if not self.head:
            return

        node = self.head
        counter = 0

        while node:
            new_data = fn(node.data, counter)
            node.data = new_data
            node = node.next
            counter += 1

    def find_index(self, data) -> int:
        if not self.head:
            return

        counter = 0
        current = self.head

        while current:
            if current.data == data:
                return counter

            current = current.next
            counter += 1

        return -1

    def contains(self, data) -> bool:
        if not self.head:
            return False

        current = self.head

        while current:
            if current.data == data:
                return True

            current = current.next

        return False

    def find(self, data) -> Node or None:
        if not self.head:
            return

        current = self.head

        while current:
            if current.data == data:
                return current

            current = current.next

        return None

    def sort(self) -> None:
        if not self.head or not self.head.next:
            return

        current = self.head
        next = None

        while current:
            next = current.next
            while next:
                if current.data > next.data:
                    temp = current.data
                    current.data = next.data
                    next.data = temp

                next = next.next

            current = current.next

    def merger(self) -> None:
        pass

    def merge_sort(self) -> None:
        pass

    def midpoint(self) -> int:
        if not self.head:
            return

        current = self.head


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.insert_first(22)
    linkedlist.insert_first(26)
    linkedlist.insert_first(76)
    print(linkedlist.get_last())
    linkedlist.remove_last()
    print(linkedlist.get_last())
    linkedlist.insert_first(56)
    linkedlist.insert_last(101)
    print(linkedlist.get_last())
    print(linkedlist.get_first())
    linkedlist.reverse()
    print(linkedlist.get_first())
    linkedlist.for_each(lambda num, index: num * 2)
    print(linkedlist.get_first())
    print(linkedlist.length())
    print(len(linkedlist))
    print(linkedlist.get_at(2))
    print(linkedlist[2])
    print(linkedlist.get_last())
    print(linkedlist)
    linkedlist.reverse()
    print(linkedlist)
    print(linkedlist)
    linkedlist.sort()
    print(linkedlist)
