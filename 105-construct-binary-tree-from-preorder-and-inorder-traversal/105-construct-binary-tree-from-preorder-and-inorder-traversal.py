# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) < 1:
            
            return None
        
        answer = TreeNode(preorder[0])
        midIndex = inorder.index(preorder[0])
        leftInorder = inorder[:midIndex]
        leftInorderSet = set(leftInorder)
        answer.left = self.buildTree([po for po in preorder[1:] if po in leftInorderSet], leftInorder)
        rightInorder = inorder[midIndex + 1:]
        rightInorderSet = set(rightInorder)
        answer.right = self.buildTree([po for po in preorder[1:] if po in rightInorderSet], rightInorder)
        
        return answer