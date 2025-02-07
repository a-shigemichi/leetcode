from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs_find_paths(self, node: TreeNode, target_sum: int, curr_sum: int, path: list[int], result: list[list[int]]) -> None:
        """
        DFS helper function to find paths that sum to target_sum.
        
        Args:
            node (TreeNode): Current node in traversal
            target_sum (int): Target sum to find
            curr_sum (int): Current sum along the path
            path (list[int]): Current path being explored
            result (list[list[int]]): List to store valid paths
        """
        curr_sum += node.val
        path.append(node.val)

        if not node.left and not node.right:
            if curr_sum == target_sum:
                result.append(path[:])
        else:
            if node.left:
                self.dfs_find_paths(node.left, target_sum, curr_sum, path, result)
            if node.right:
                self.dfs_find_paths(node.right, target_sum, curr_sum, path, result)
        
        path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        """
        Find all root-to-leaf paths where path sum equals targetSum.
        
        Args:
            root (TreeNode): Root node of the binary tree
            targetSum (int): Target sum to find in paths
            
        Returns:
            list[list[int]]: List of paths (each path is a list of node values)
            that sum to targetSum
            
        Example:
            Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
            Output: [[5,4,11,2],[5,8,4,5]]
            
            Input: root = [1,2,3], targetSum = 5
            Output: []
        """
        if not root:
            return []
        
        result = []
        self.dfs_find_paths(root, targetSum, 0, [], result)
        return result