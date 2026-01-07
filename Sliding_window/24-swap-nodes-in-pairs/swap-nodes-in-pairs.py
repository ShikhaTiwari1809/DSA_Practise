# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            nxt = b.next

            # swap
            prev.next = b
            b.next = a
            a.next = nxt

            # move prev to the end of swapped pair
            prev = a

        return dummy.next
        