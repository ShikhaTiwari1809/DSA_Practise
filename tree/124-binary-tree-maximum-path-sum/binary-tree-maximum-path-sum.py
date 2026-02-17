# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.sum = float('-inf')

        def maxSum(node):
            if not node:
                return 0

            left_sum = max(0, maxSum(node.left))
            right_sum = max(0,maxSum(node.right))

            # diameter passing through this node = left height + right height
            self.sum = max(self.sum, left_sum + right_sum + node.val)

            # return height for parent's computation
            return node.val + max(left_sum, right_sum)

        maxSum(root)
        return self.sum