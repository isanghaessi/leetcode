# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            
            return head
        
        answer = ListNode()
        answer.next = head
        node = answer
        index = 0
        while index < left - 1:
            node = node.next
            index += 1
        leftNode, rightNode = node, node.next
        p, q, r = node, node.next, node.next
        while index < right:
            r, q.next = r.next, p
            p, q = q, r
            index += 1
        leftNode.next, rightNode.next = p, r
        
        return answer.next