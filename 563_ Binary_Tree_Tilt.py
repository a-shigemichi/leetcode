import unittest
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_tilt(self, root: Optional[TreeNode]) -> int:
        """
        Received the root of a binary tree, return the sum of every tree node's tilt.
        The tilt of a tree node is the absolute difference between the sum of all left subtree node values 
        and all right subtree node values. 
        
        Args:
            root(Optional[TreeNode]): Root node of the binary tree.

        Returns:
            int: The sum of every tree node's tilt.
        """
        self.total_tilt = 0       
        
        self.calculate_total_tilt_sum(root)
        return self.total_tilt

    def calculate_total_tilt_sum(self, node: Optional[TreeNode]) -> int:
        """
        Calculate the sum of all node values in a subtree while accumulating tilt values.

        Args:
            node(Optional[TreeNode]): Root node of the current subtree.

        Returns:
            int: Sum of all node values in the current subtree.
        """
        if not node:
            return 0
        
        left_sum = self.calculate_total_tilt_sum(node.left)
        right_sum = self.calculate_total_tilt_sum(node.right)
        
        tilt = abs(left_sum - right_sum)
        self.total_tilt += tilt
        
        return left_sum + right_sum + node.val
    

class TestBinaryTreeTilt(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def array_to_tree(self, array: List[Optional[int]], node_position: int = 0) -> Optional[TreeNode]:
        """Convert array representation to binary tree"""
        if node_position >= len(array) or array[node_position] is None:
            return None
        
        root = TreeNode(array[node_position])
        root.left = self.array_to_tree(array, 2 * node_position + 1)
        root.right = self.array_to_tree(array, 2 * node_position + 2)
        
        return root

    def test_tree_1(self):
        """Test example 1"""
        root = self.array_to_tree([1, 2, 3])
        self.assertEqual(self.solution.find_tilt(root), 1)
    
    def test_tree_2(self):
        """Test example 2"""
        root = self.array_to_tree([4, 2, 9, 3, 5, None, 7])
        self.assertEqual(self.solution.find_tilt(root), 15)
    
    def test_tree_3(self):
        """Test example 3"""
        root = self.array_to_tree([21, 7, 14, 1, 1, 2, 2, 3, 3])
        self.assertEqual(self.solution.find_tilt(root), 9)

    def test_empty_tree(self):
        """Test an empty tree"""
        self.assertEqual(self.solution.find_tilt(None), 0)

if __name__ == '__main__':
    unittest.main() 
