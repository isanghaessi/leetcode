from heapq import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heapQ = []
        for l in lists:
            while l:
                heappush(heapQ, l.val)
                l = l.next
        answer = node = ListNode()
        while len(heapQ):
            node.next = ListNode((heappop(heapQ)))
            node = node.next
            
        return answer.next