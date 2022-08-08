from heapq import *

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for h, k in people:
            heappush(heap, (-h, k))
        answer = []
        while len(heap) > 0:
            h, k = heappop(heap)
            answer.insert(k, (-h, k))
        
        return answer