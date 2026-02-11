# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        
        q = deque([root])
        average =[]
        while q:
            level_avg =[]
            for _ in range(len(q)):
                node = q.popleft()
                level_avg.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            cur_avg = sum(level_avg)/len(level_avg)
            average.append(cur_avg)
        
        return average