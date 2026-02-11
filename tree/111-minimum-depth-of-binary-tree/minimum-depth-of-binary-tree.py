# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        q = deque([root])
        depth_val = []
        depth =0
        while q:
            
            
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.left is None and node.right is None:
                    depth_val.append(depth+1)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth+=1
            
        return min(depth_val)
        