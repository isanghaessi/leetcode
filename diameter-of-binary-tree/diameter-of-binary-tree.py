# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def preOrder(node, length):
            if node == None:
                
                return length
            left_length = preOrder(node.left, length)
            right_length = preOrder(node.right, length)
            self.result = max(self.result, left_length + right_length)
            
            return max(left_length + 1, right_length + 1)

        preOrder(root, 0)
        
        return self.result