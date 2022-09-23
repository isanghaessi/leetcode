# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) < 1:
            
            return None
        
        answer = TreeNode(preorder.pop(0))
        midIndex = inorder.index(answer.val)
        answer.left = self.buildTree(preorder, inorder[:midIndex])
        answer.right = self.buildTree(preorder, inorder[midIndex + 1:])
        
        return answer