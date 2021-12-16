# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root1, root2):
            if not root1 and not root2:
                
                return
            if not root1:
                root1 = TreeNode()
            if root2:
                root1.val += root2.val
            if not root1.left and root2 and root2.left:
                root1.left = TreeNode()
            if not root1.right and root2 and root2.right:
                root1.right = TreeNode()
            root1.left = dfs(root1.left, root2.left if root2 else root2)
            root1.right = dfs(root1.right ,root2.right if root2 else root2)
            
            return root1
        
        
        return dfs(root1, root2)