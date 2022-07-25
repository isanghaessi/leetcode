# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = True
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, height):
            if not node:
                
                return height
            
            leftHeight = dfs(node.left, height)
            rightHeight = dfs(node.right, height)
            if abs(leftHeight - rightHeight) > 1:
                self.answer = False
                
            return max(leftHeight, rightHeight) + 1
        
        
        dfs(root, 0)
        
        return self.answer