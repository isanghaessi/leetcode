# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headNode = head
        even = evenNode = ListNode()
        while headNode != None and headNode.next != None:
            next = headNode.next
            headNode.next, next.next, evenNode.next = next.next, None, next
            if headNode.next == None:
                
                break
            headNode, evenNode = headNode.next, evenNode.next
        if headNode != None:
            headNode.next = even.next
        
        return head
        