import unittest
from main import LinkedList, Node


class NodeTest(unittest.TestCase):
    def test_node_is_a_class(self):
        self.assertIsInstance(Node, object)

    def test_node_has_right_properties(self):
        node = Node('a', 'b')
        self.assertEqual(node.data, 'a')
        self.assertEqual(node.next, 'b')


class LinkedListTest(unittest.TestCase):
    def test_list_is_a_class(self):
        self.assertIsInstance(LinkedList, object)

    def test_insert_first(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.head.data, 1)
        linkedlist.insert_first(2)
        self.assertEqual(linkedlist.head.data, 2)

    def test_length(self):
        linkedlist = LinkedList()
        self.assertEqual(linkedlist.length(), 0)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.length(), 4)

    def test_get_first(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.head.data, 1)
        linkedlist.insert_first(2)
        self.assertEqual(linkedlist.head.data, 2)

    # def test_get_last(self):
    #     linkedlist = LinkedList()
    #     linkedlist.insert_first(1)


unittest.main()
