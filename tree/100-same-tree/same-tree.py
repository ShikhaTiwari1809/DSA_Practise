# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        dq = deque([(p, q)])

        while dq:
            
            for _ in range(len(dq)):
                a, b = dq.popleft()

                if a is None and b is None:
                    continue
                if a is None or b is None:
                    return False
                if a.val != b.val:
                    return False
                
                dq.append((a.left, b.left))
                dq.append((a.right, b.right))


        return True   
        