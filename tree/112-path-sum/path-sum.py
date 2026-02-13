# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        stack = [(root, root.val)]
        curSum = 0

        while stack:
            
            node, s = stack.pop()
           
            if not node.left and not node.right and s == targetSum:
                return True
            
            if node.right:
                stack.append((node.right, s + node.right.val))
            if node.left:
                stack.append((node.left, s + node.left.val))

        return False

            
