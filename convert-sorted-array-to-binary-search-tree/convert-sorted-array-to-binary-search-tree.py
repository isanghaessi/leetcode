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
        
        
        def divide(nums, root):
            
            if len(nums) < 1:
                
                return root
            mid_index = len(nums) // 2
            root = insert(root, nums[mid_index])
            root = divide(nums[:mid_index], root)
            root = divide(nums[mid_index + 1:], root)
            
            return root
        
        
        return divide(nums, None)