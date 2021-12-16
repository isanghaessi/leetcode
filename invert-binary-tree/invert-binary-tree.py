# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def pre_order_filter(root):
            if not root or root.val == float('inf'):
                
                return None
            root.left = pre_order_filter(root.left)
            root.right = pre_order_filter(root.right)
            
            return root
        
        
        if not root:
            
            return root
        q = []
        q.append(root)
        num_of_nodes = 1
        while len(list(filter(lambda a: a.val != float('inf'), q))) > 0:
            for i in range(len(q) // 2):
                q[i].val, q[-(i + 1)].val = q[-(i + 1)].val, q[i].val
            new_q = []
            while len(q) > 0:
                current_node = q.pop()
                if not current_node.left:
                    current_node.left = TreeNode(float('inf'))
                if not current_node.right:
                    current_node.right = TreeNode(float('inf'))
                new_q.append(current_node.left)
                new_q.append(current_node.right)
            q = new_q
        root = pre_order_filter(root)
        
        return root