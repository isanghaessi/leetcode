# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = float('-inf')
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def findMax(node):
            global result
            
            if node == None:
                
                return float('-inf')
            leftSum = findMax(node.left)
            rightSum = findMax(node.right)
            self.result = max(self.result, node.val, leftSum + node.val, node.val + rightSum, leftSum + node.val + rightSum)
            
            return max(node.val, node.val + max(leftSum, rightSum))
        
        
        leftMax = findMax(root.left)
        rightMax = findMax(root.right)
        
        print(self.result, leftMax, rightMax, leftMax + root.val + rightMax)
        
        return max(self.result, leftMax, rightMax, root.val, leftMax + root.val, root.val + rightMax, leftMax + root.val + rightMax)