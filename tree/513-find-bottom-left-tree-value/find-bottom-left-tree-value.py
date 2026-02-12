# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # BFS Technique on this I will append right value first so at each level values will be from right to left and last value will
        # be the leftmost value , instead of using that we can also do normal left to right and just use ans = q[0].val basically at     each level pick first value outside for loop
        q = deque([root])
        left_node = None

        while q:
            #ans = q[0].val 
            for _ in range(len(q)):
                
                node = q.popleft()
                left_node = node.val

                if node.right:
                    q.append(node.right)
                
                if node.left:
                    q.append(node.left)
                
        
        return left_node

        # DFS Technique in this we will store max_depth and at each level we will only xhnage the answer value if we have not seen the that level or only higher value since we are doing left first so at each depth we will get left most value of that depth level.
        self.max_depth = -1
        self.answer = 0
        
        def dfs(node, depth):
            if not node:
                return
            
            if depth > self.max_depth:
                self.max_depth = depth
                self.answer = node.val
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return self.answer