import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            
            return True
        queue = collections.deque([root])
        while len(queue) > 0:
            queueVals = [q.val for q in queue]
            if queueVals != queueVals[::-1]:
                
                return False
            nextQueue = collections.deque([])
            while len(queue):
                node = queue.pop()
                if node.val != 'null':
                    nextQueue.append(node.left if node.left != None else TreeNode('null'))
                    nextQueue.append(node.right if node.right != None else TreeNode('null'))
            queue = nextQueue
        
        return True
            