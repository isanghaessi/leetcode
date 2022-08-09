from heapq import *

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            
            return -1
        
        calCost = []
        i = 0
        while i < len(gas):
            calCost.append(gas[i] - cost[i])
            i += 1
        heap = []
        for i, cc in enumerate(calCost):
            heappush(heap, (-cc, i))
        while len(heap) > 0:
            _, start = heappop(heap)
            i = start
            current = calCost[i]
            i = (i + 1) % len(calCost)
            while i != start and current >= 0:
                current += calCost[i]
                i = (i + 1) % len(calCost)
            if i == start and current >= 0:
                
                return start