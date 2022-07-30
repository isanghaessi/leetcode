# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            
            return None
        
        midIndex = len(nums) // 2
        answer = TreeNode(nums[midIndex])
        answer.left = self.sortedArrayToBST(nums[:midIndex])
        answer.right = self.sortedArrayToBST(nums[midIndex + 1:])
        
        return answer