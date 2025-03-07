from typing import Optional, List

class TreeNode:
    def __init__(self, val: Optional[int] = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determine if a binary tree is height-balanced.
        
        A height-balanced binary tree is a binary tree in which the depth of the two 
        subtrees of every node never differs by more than 1.
        
        Args:
            root (Optional[TreeNode]): The root node of the binary tree.
            
        Returns:
            bool: True if the binary tree is height-balanced, False otherwise.
        """
        return self.compute_balance_height(root)
    
    def compute_balance_height(self, node: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is height-balanced.
        
        Args:
            node (Optional[TreeNode]): The root node of the binary tree to check.
            
        Returns:
            bool: True if the binary tree is height-balanced, False otherwise.
        """
        if not node:
            return True

        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)
        
        # Check if height difference is at most 1 and both subtrees are balanced
        if (abs(left_height - right_height) <= 1 and 
            self.compute_balance_height(node.left) and 
            self.compute_balance_height(node.right)):
            return True
            
        return False
    
    def calculate_height(self, node: Optional[TreeNode]) -> int:
        """
        Calculate the height of a binary tree.
        
        Args:
            node (Optional[TreeNode]): The root node of the binary tree.
            
        Returns:
            int: The height of the tree. Empty tree has height 0.
        """
        if not node:
            return 0
            
        # Recursive case: height is max of left and right subtrees + 1
        return max(self.calculate_height(node.left), self.calculate_height(node.right)) + 1
    


class TestSolution:
    def array_to_tree(self, array: List[Optional[int]], node_position: int = 0) -> Optional[TreeNode]:
        """
        Convert array representation to binary tree recursively.
        
        Args:
            array (List[Optional[int]]): Array representation of the binary tree.
            node_position (int): Current position in the array.
            
        Returns:
            Optional[TreeNode]: Root of the binary tree.
        """
        if node_position >= len(array) or array[node_position] is None:
            return None
        
        root = TreeNode(array[node_position])
        root.left = self.array_to_tree(array, 2 * node_position + 1)
        root.right = self.array_to_tree(array, 2 * node_position + 2)
        
        return root
    def setup_method(self):
        self.solution = Solution()
    
    def test_isBalanced_empty_tree(self):
        # Test case with an empty tree
        assert self.solution.isBalanced(None) == True
    
    def test_isBalanced_single_node(self):
        # Test case with a single node
        root = self.array_to_tree([1])
        assert self.solution.isBalanced(root) == True
    
    def test_isBalanced_balanced_tree(self):
        # Test case with a balanced tree
        root = self.array_to_tree([3, 9, 20, None, None, 15, 7])
        assert self.solution.isBalanced(root) == True
    
    def test_isBalanced_unbalanced_tree(self):
        # Test case with a unbalanced tree
        root = self.array_to_tree([1, 2, 2, 3, 3, None, None, 4, 4])
        assert self.solution.isBalanced(root) == False
