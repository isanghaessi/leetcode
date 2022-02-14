# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        prev, current = None, head
        for _ in range(count - n):
            prev, current = current, current.next
        if prev:
            prev.next = current.next
        
            return head
        else:
            
            return current.next