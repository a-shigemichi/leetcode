from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Converts a binary search tree to a balanced binary search tree.
        
        A balanced BST is one where the depth of the two subtrees of 
        every node never differs by more than 1.
        
        Approach:
        1. Perform inorder traversal to get sorted values.
        2. Build balanced BST from sorted array using divide and conquer.
        
        Args:
            root: Root node of the input BST
            
        Returns:
            Root node of the balanced BST
        """
        if not root:
            return None

        values = []
        self.inorder(root, values)

        return self.build_balanced_bst(values, 0, len(values) - 1)
    
    def inorder(self, node: Optional[TreeNode], values: List[int]) -> None:
        """
        Performs inorder traversal to collect node values in sorted order.
        
        Args:
            node: Current node being visited
            values: List to store the node values
        """
        if not node:
            return

        self.inorder(node.left, values)
        values.append(node.val)
        self.inorder(node.right, values)
    
    def build_balanced_bst(self, values: List[int], left: int, 
                           right: int) -> Optional[TreeNode]:
        """
        Builds a balanced BST from a sorted array using divide and conquer.
        
        Args:
            values: Sorted array of values
            left: Left boundary index
            right: Right boundary index
            
        Returns:
            Root node of the balanced subtree
        """
        if left > right:
            return None

        # Choose middle element as root to ensure balance
        mid = left + (right - left) // 2
        root = TreeNode(values[mid])

        # Recursively build left and right subtrees
        root.left = self.build_balanced_bst(values, left, mid - 1)
        root.right = self.build_balanced_bst(values, mid + 1, right)

        return root
