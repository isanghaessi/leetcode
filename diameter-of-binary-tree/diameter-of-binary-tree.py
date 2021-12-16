# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, count):
            nonlocal answer
            
            if node == None:
                
                return count
            
            left = dfs(node.left, count + 1)
            right = dfs(node.right, count + 1)
            answer = max(answer, left + right - count * 2 - 2)
            
            return max(left, right)

            
        if not root:
            
            return 0
        answer = 0
        left = dfs(root.left, 0)
        right = dfs(root.right, 0)
        answer = max(answer, left + right)
        
        return answer