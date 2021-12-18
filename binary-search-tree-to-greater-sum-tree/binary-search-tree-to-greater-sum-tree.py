# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def in_order(node, sum_of_right):
            if not node:
                
                return sum_of_right
            node.val += in_order(node.right, sum_of_right)
            
            return in_order(node.left, node.val)
            
        
        in_order(root, 0)
        
        return root