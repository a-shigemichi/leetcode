# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        Delete a node from singly-linked list without access to head.
        Copy next node's value to current node and skip next node.
        
        Args:
            node (ListNode): The node to be deleted
        """
        node.val = node.next.val

        node.next = node.next.next
        