# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = previous = ListNode(float('-inf'))
        result.next = current = head
        while current:
            move = result
            nextCurrent = current.next
            while move.next and move.next.val <= current.val and move.next is not current:
                move = move.next
            if move.next and move.next is not current:
                previous.next = current.next
                move.next, current.next =  current, move.next
            current = nextCurrent
            previous = result
            while previous.next is not current:
                previous = previous.next
        
        return result.next