import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            
            return []
        result = []
        queue = collections.deque([root])
        while len(queue) > 0:
            result.append([q.val for q in queue])
            nextQueue = collections.deque([])
            while len(queue)> 0:
                node = queue.popleft()
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            queue = nextQueue
            
        return result