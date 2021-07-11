# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfsLongest(node, length):
            if node == None:
                
                return None, length
            left_v, left_l = dfsLongest(node.left, length)
            right_v, right_l = dfsLongest(node.right, length)
            if left_v == right_v == node.val:
                length = max(left_l, right_l) + 1
                self.result = max(self.result, left_l + right_l + 2)
            elif left_v == node.val:
                length = left_l + 1
            elif right_v == node.val:
                length = right_l + 1
            else:
                length = 0
            self.result = max(self.result, length)
                
            return node.val, length
            
            
        dfsLongest(root, 0)
        
        return self.result