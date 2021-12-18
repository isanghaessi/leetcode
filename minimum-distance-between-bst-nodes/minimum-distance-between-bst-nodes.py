# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def pre_order(node, min_val, max_val):
            nonlocal answer
            
            if not node:
                
                return min_val, max_val
            lmin_val, lmax_val = pre_order(node.left, node.val, node.val)
            rmin_val, rmax_val = pre_order(node.right, node.val, node.val)
            if lmax_val < node.val:
                answer = min(answer, node.val - lmax_val)
            if rmin_val > node.val:
                answer = min(answer, rmin_val - node.val)
            
            return lmin_val, rmax_val
        
        
        answer = float('inf')
        pre_order(root, root.val, root.val)
        
        return answer
            