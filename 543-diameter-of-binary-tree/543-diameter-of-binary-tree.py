# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if not node:
                
                return depth
            
            leftDepth = dfs(node.left, depth)
            rightDepth = dfs(node.right, depth)
            maxDepth = max(leftDepth, rightDepth)
            if leftDepth == 0 or rightDepth == 0:
                self.answer = max(self.answer, maxDepth)
            else:
                self.answer = max(self.answer, leftDepth + rightDepth)
            
            return maxDepth + 1
        
        
        dfs(root, 0)

        return self.answer