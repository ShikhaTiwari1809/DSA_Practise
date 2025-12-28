# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def reverse(reversehead):
            curr = reversehead
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr =nxt
            return prev
        

        # reverse the second half
        rev_head = reverse(head)

        curr = rev_head
        cnt =1
        prev = None

        
        while curr:
            if n ==1:
                rev_head = rev_head.next
                break
            if cnt ==n:
                prev.next = curr.next
            prev = curr
            curr = curr.next
            cnt +=1
        
        print(rev_head)
        return reverse(rev_head)
        