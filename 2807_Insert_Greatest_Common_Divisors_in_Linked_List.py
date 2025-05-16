# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Insert nodes with the greatest common divisor between adjacent nodes in a linked list.
        
        Given the head of a linked list, insert a new node with a value equal to the greatest common divisor
        of each pair of adjacent nodes, between those nodes.
        
        Args:
            head: The head of a linked list
            
        Returns:
            Optional[ListNode]: The head of the modified linked list after insertion
            
        Example:
            Input: head = [18,6,10,3]
            Output: [18,6,6,2,10,1,3]
            Explanation: GCD of 18 and 6 = 6, GCD of 6 and 10 = 2, GCD of 10 and 3 = 1
        """
        if not head or not head.next:
            return head
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        current = head
        
        while current and current.next:
            gcd_value = gcd(current.val, current.next.val)
            
            new_node = ListNode(gcd_value)
            
            new_node.next = current.next
            current.next = new_node
            
            current = new_node.next
        
        return head