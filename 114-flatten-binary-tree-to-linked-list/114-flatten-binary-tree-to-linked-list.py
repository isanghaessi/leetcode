# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatten(node):
            if node == None:
                
                return None
            node.left = flatten(node.left)
            node.right = flatten(node.right)
            if node.left != None:
                leftNodeLeaf= node.left
                while leftNodeLeaf.right != None:
                    leftNodeLeaf = leftNodeLeaf.right
                node.right, leftNodeLeaf.right = node.left, node.right
                node.left = None
            
            return node
        
        
        flatten(root)