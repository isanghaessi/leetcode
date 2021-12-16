import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            
            return 0
        answer = 1
        q = collections.deque()
        q.append((root, 1))
        while len(q) > 0:
            answer = q[-1][1]
            new_q = collections.deque()
            while len(q) > 0:
                current, height = q.pop()
                if current.left:
                    new_q.appendleft((current.left, height + 1))
                if current.right:
                    new_q.appendleft((current.right, height + 1))
            q = new_q
            
        
        return answer