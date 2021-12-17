# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            nonlocal answer
            
            if not answer or not node:
                
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                
                answer = False
            return max(left, right) + 1
        
        answer = True
        dfs(root)
        
        return answer