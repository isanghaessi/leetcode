# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def order(node):
            if not node:
                
                return
            
            if node.val < low:
                order(node.right)
            elif node.val > high:
                order(node.left)
            else:
                self.answer += node.val
                order(node.left)
                order(node.right)
        
        
        order(root)
        
        return self.answer