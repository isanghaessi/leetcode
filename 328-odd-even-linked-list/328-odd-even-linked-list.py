# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            
            return None
        
        odd = oddTail = ListNode()
        node = head
        while node and node.next:
            node.next, oddTail.next, oddTail = node.next.next, node.next, node.next
            oddTail.next = None
            node = node.next
        node = head
        while node.next:
            node = node.next
        node.next = odd.next
        
        return head
