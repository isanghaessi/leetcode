# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            
            return None
        
        left, right = head, head.next
        answer = previous = ListNode()
        previous.next = left
        while left and right:
            right.next, left.next, previous.next, previous, left, right = left, right.next, right, left, left.next.next, (right.next.next if right.next else None)
        
        return answer.next