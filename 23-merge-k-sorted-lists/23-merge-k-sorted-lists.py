from heapq import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heapQ = []
        for i, l in enumerate(lists):
            if l:
                heappush(heapQ, (l.val, i, l))
        answer = node = ListNode()
        while len(heapQ) > 0:
            value, i, head = heappop(heapQ)
            node.next = ListNode(value)
            node = node.next
            if head and head.next:
                heappush(heapQ, (head.next.val, i, head.next))
        
        return answer.next