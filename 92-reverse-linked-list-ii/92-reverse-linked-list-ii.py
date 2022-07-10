# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        answer = ListNode()
        answer.next = head
        node = answer
        for _ in range(left - 1):
            node = node.next
        leftNode = node
        node = firstNode = node.next
        p, q, r = node, node.next, node.next
        for i in range(right - left):
            r, q.next = r.next, p
            p, q = q, r
        leftNode.next, firstNode.next = p, q
        
        return answer.next