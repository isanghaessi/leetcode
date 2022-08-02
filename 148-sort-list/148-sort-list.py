# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head):
            result = ListNode()
            result.next = head
            count = 0
            slow = fast = head
            previousSlow = None
            while fast:
                if fast.next:
                    previousSlow = slow
                    slow = slow.next
                    fast = fast.next.next
                    count += 2
                else:
                    break
            if count == 0:
                
                return head
            else:
                previousSlow.next = None
                
                return _merge(merge(head), merge(slow))
            
            
        def _merge(node1, node2):
            result = node =  ListNode()
            while node1 and node2:
                if node1.val < node2.val:
                    node.next = ListNode(node1.val)
                    node1 = node1.next
                else:
                    node.next = ListNode(node2.val)
                    node2 = node2.next
                node = node.next
            while node1:
                node.next = ListNode(node1.val)
                node1 = node1.next
                node = node.next
            while node2:
                node.next = ListNode(node2.val)
                node2 = node2.next
                node = node.next
            
            return result.next
            
            
        return merge(head)