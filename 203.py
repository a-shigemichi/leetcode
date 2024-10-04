class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class Solution(object):
    def removeElements(self, head, val):
        head = create_linked_list(head)
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return linked_list_to_list(dummy.next)
    
def main():
    head = [1,2,6,3,4,5,6]
    val = 6
    my_object = Solution()        
    judgement = my_object.removeElements(head,val)
    print(judgement)

if __name__ == "__main__":
   main()