# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        stack = [(root, [root.val])]
        result =[]

        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:
                result.append('->'.join(str(item) for item in path))
                continue
            if node.right:
                stack.append((node.right, path + [node.right.val]))

            if node.left:
                stack.append((node.left, path +[node.left.val]))

        
        return result

        