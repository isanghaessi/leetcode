# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        node = answer
        while head:
            nextHead = head.next
            while node.next and node.next.val < head.val:
                node = node.next
            node.next, head.next = head, node.next
            head = nextHead
            if head and node.val > head.val:
                node = answer
        
        return answer.next