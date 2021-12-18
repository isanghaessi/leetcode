# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def search(node):
            nonlocal answer
            
            if not node:
                
                return
            if node.val < low:
                search(node.right)
            elif low <= node.val and node.val <= high:
                answer += node.val
                search(node.left)
                search(node.right)
            else:
                search(node.left)
                
        
        answer = 0
        search(root)
        
        return answer