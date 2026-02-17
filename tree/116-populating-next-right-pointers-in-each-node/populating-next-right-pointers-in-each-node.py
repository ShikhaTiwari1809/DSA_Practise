"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        curr , nxt = root, root.left if root else None

        while curr and nxt:
            curr.left.next = curr.right

            if curr.next:
                curr.right.next = curr.next.left
            
            curr = curr.next

            if not curr:
                curr = nxt
                nxt = curr.left
        return root        
        
        
        
        
        
        
        
        # I solved first uding below statemnt but it will take O(n) space to have to optimize and work for O(1) space 
        # In below we are traversing to each levelnode and once we have data of all node at leevl we will assign the next one
        # if not root:
        #     return root
        
        # q = deque([root])

        # while q:
        #     levelnode =[]
        #     for i in range(len(q)):
        #         node = q.popleft()
                
        #         levelnode.append(node)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
            
        #     for i in range(len(levelnode)):
        #         if i == len(levelnode)-1:
        #             levelnode[i].next = None
        #         else:
        #             levelnode[i].next = levelnode[i+1]
   

        # return root
    