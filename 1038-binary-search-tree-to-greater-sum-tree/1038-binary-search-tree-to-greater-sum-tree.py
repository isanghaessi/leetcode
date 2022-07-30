# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    rightSum = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def order(node):
            if not node:
                
                return

            order(node.right)
            self.rightSum += node.val
            node.val = self.rightSum
            order(node.left)
        
        
        order(root)
        
        return root