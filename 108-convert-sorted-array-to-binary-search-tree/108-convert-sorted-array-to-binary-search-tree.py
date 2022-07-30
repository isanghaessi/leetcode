# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def insert(node, num):
            if not node:
                
                return TreeNode(num)
            
            if num <= node.val:
                node.left = insert(node.left, num)
            else:
                node.right = insert(node.right, num)
            
            return node
        
        if len(nums) == 0:
            
            return None
        
        midIndex = len(nums) // 2
        answer = TreeNode(nums[midIndex])
        answer.left = self.sortedArrayToBST(nums[:midIndex])
        answer.right = self.sortedArrayToBST(nums[midIndex + 1:])
        
        return answer