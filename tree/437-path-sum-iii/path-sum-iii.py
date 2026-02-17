# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        stack = [(root, [root.val])]
        result =[]
        count = 0

        while stack:
            node, path = stack.pop()
            
            s = 0
            for i in range(len(path) - 1, -1, -1):
                s += path[i]
                if s == targetSum:
                    count += 1
            
            if node.right:
                stack.append((node.right, path+[node.right.val]))
            if node.left:
                stack.append((node.left, path+[node.left.val]))
        
        
     
        return count