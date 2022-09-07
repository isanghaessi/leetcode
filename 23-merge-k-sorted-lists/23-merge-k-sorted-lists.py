from heapq import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heapQ = []
        for node in lists:
            while node != None:
                heappush(heapQ, node.val)
                node = node.next
        answer = node = ListNode()
        while len(heapQ) > 0:
            node.next = ListNode(heappop(heapQ))
            node = node.next
        
        return answer.next