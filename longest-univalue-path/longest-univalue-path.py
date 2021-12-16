# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal answer
            
            if not node:
                
                return None, 0
            left_val, left_count = dfs(node.left)
            right_val, right_count = dfs(node.right)
            answer_count = 1
            return_count = 1
            if left_val == node.val:
                answer_count += left_count
                return_count += left_count
            if right_val == node.val:
                answer_count += right_count
                return_count = max(return_count, right_count + 1)
            answer = max(answer, answer_count - 1)
            
            return node.val, return_count
        
        if not root:
            
            return 0
        answer = 0
        dfs(root)
        
        return answer