import unittest

from linked_list import *

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = linked_list()

    def test_sum_empty(self):
        self.assertEqual(self.ll.sumNodes(), 0)

    def test_sum_single_node(self):
        self.ll.insertEnd(Node(5))
        self.assertEqual(self.ll.sumNodes(), 5)

    def test_sum_multiple_nodes(self):
        self.ll.insertEnd(Node(5))
        self.ll.insertEnd(Node(10))
        self.ll.insertEnd(Node(15))
        self.assertEqual(self.ll.sumNodes(), 30)

    def test_sum_negative_nodes(self):
        self.ll.insertEnd(Node(-5))
        self.ll.insertEnd(Node(-10))
        self.ll.insertEnd(Node(-15))
        self.assertEqual(self.ll.sumNodes(), -30)

if __name__ == '__main__':
    unittest.main()