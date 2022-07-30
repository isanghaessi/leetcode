# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            
            return None
        
        headVal = preorder[0]
        if len(preorder) == 1 and len(inorder) == 1:
            
            return TreeNode(headVal)
        
        ioIndex = inorder.index(headVal)
        ioLeft = inorder[:ioIndex]
        ioRight = inorder[ioIndex + 1:]
        poLeft = []
        if len(ioLeft) > 0:
            i = 1
            while len(ioLeft) > len(poLeft):
                poLeft.append(preorder[i])
                i += 1
        poRight = []
        if len(ioRight) > 0:
            i = 1
            while preorder[i] in poLeft:
                i += 1
            while i < len(preorder):
                poRight.append(preorder[i])
                i += 1
        answer = TreeNode(headVal)
        if len(ioLeft) > 0:
            answer.left = self.buildTree(poLeft, ioLeft)
        if len(ioRight) > 0:
            answer.right = self.buildTree(poRight, ioRight)
        
        return answer
        