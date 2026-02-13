# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Iterative solution
        def iterativeReverse():
            if not root:
                return []

            stack = [root]
            result = []

            while stack:
                node = stack.pop()
                result.append(node.val)          # Root first
                
                if node.left:
                    stack.append(node.left)   # push left
                if node.right:
                    stack.append(node.right)  # push right (so right is processed first)

            return result[::-1]
        
        def iterativeLastVisited():
            #Iterative solution with last visisted without reversing

            result = []
            stack = []
            curr = root
            lastVisited = None

            while curr or stack:
                # go left as far as possible
                while curr:
                    stack.append(curr)
                    curr = curr.left

                node = stack[-1]  # peeking, don't pop yet

                # if right child exists and not processed yet, go right
                if node.right and lastVisited != node.right:
                    curr = node.right
                else:
                    # both children done- visit node
                    stack.pop()
                    result.append(node.val)
                    lastVisited = node

            return result      
            
        def recursive():
            #Recursive solution

            result =[]

            def dfs(node):
                if node is None:
                    return
                dfs(node.left)
                dfs(node.right)
                result.append(node.val)
            dfs(root)

            return result

        
        #return iterativeLastVisited()
        #return iterativeReverse()
        return recursive()