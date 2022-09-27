# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1, l2):
            result = node =  ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    val, l1 = l1.val, l1.next
                else:
                    val, l2 = l2.val, l2.next
                node.next = ListNode(val)
                node = node.next
            while l1:
                node.next, l1 = ListNode(l1.val), l1.next
                node = node.next
            while l2:
                node.next, l2 = ListNode(l2.val), l2.next
                node = node.next
            
            return result.next
        
        
        if not head or not head.next:
            
            return head
        
        answer = ListNode()
        answer.next = head
        prev =  answer
        slow = fast = head
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        return merge(self.sortList(head), self.sortList(slow))
        
        