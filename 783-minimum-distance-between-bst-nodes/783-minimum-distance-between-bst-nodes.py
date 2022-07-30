# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = float('inf')
    previous = float('inf')
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def order(node):
            if not node:
                
                return
            
            order(node.right)
            currentDifference = self.previous - node.val
            if currentDifference < self.answer:
                self.answer = currentDifference
            self.previous = node.val
            order(node.left)
        
        
        order(root)
        
        return self.answer