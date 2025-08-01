# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Codec:
    def serialize(self, root: Optional['TreeNode']) -> str:
        """
        Encodes a tree to a single string.
        
        Uses preorder traversal to serialize the binary tree into a string format.
        Null nodes are represented as 'null' to maintain tree structure.
        
        Args:
            root: Optional[TreeNode] - The root of the binary tree to serialize
            
        Returns:
            str - Comma-separated string representation of the tree
        """
        def preorder(node: Optional['TreeNode']) -> str:
            if not node:
                return "null"
            return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
        
        return preorder(root)

    def deserialize(self, data: str) -> Optional['TreeNode']:
        """
        Decodes your encoded data to tree.
        
        Reconstructs the binary tree from the serialized string using preorder traversal.
        Maintains an iterator to track current position in the data stream.
        
        Args:
            data: str - Comma-separated string representation of the tree
            
        Returns:
            Optional[TreeNode] - The root of the reconstructed binary tree
        """
        def build_tree() -> Optional['TreeNode']:
            val = next(values)
            if val == "null":
                return None
            
            node = TreeNode(int(val))
            node.left = build_tree()
            node.right = build_tree()
            return node
        
        values = iter(data.split(","))
        return build_tree()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
