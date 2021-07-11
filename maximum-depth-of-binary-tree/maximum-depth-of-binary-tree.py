# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    
    def maxDepth(self, root: TreeNode) -> int:
        def checkDepth(tree, depth):
            if tree == None:
                
                return
            if tree.left == None and tree.right == None:
                
                self.result = max(self.result, depth)
            checkDepth(tree.left, depth + 1)
            checkDepth(tree.right, depth + 1)
            
        
        checkDepth(root, 1)
        
        return self.result