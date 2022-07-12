from heapq import *
from collections import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heapQ = []
        listDict = defaultdict(list)
        for l in [l for l in lists if l]:
            listDict[l.val].append(l)
            heappush(heapQ, l.val)
        answer = node = ListNode()
        while len(heapQ) > 0:
            value = heappop(heapQ)
            node.next = ListNode(value)
            node = node.next
            valueHead = listDict[value].pop()
            if valueHead and valueHead.next:
                listDict[valueHead.next.val].append(valueHead.next)
                heappush(heapQ, valueHead.next.val)
        
        return answer.next