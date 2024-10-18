# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head

def create_linked_list(elements):
    dummy = ListNode(0)
    current = dummy
    for e in elements:
        current.next = ListNode(e)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def main():
    head = [1,2,2,3]
    my_object = Solution()        
    judgement = my_object.deleteDuplicates(head)
    print(judgement)

if __name__ == "__main__":
   main()