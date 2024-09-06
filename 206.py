# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev



def main():
    head = [1,2,3,4,5]
    my_object = Solution()        
    judgement = my_object.reverseList(head)
    print(judgement)

if __name__ == "__main__":
   main()