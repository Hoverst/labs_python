import unittest
from lab3 import BinaryTree 

class TestSumOfDepths(unittest.TestCase):

    def test_single_node_tree(self):
        root = BinaryTree(10)
        self.assertEqual(root.sum_of_depths(), 0)

    def test_example_tree(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.right = BinaryTree(40)
        
        self.assertEqual(root.sum_of_depths(), 4)

    def test_balanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2, BinaryTree(4), BinaryTree(5))
        root.right = BinaryTree(3, BinaryTree(6), BinaryTree(7))
        
        self.assertEqual(root.sum_of_depths(), 10)

    def test_linear_tree(self):
        root = BinaryTree(1)
        root.right = BinaryTree(2)
        root.right.right = BinaryTree(3)
        
        self.assertEqual(root.sum_of_depths(), 3)

if __name__ == '__main__':
    unittest.main()