from heapq import *

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            
            return -1
        
        answer = 0
        current = 0
        for i in range(len(gas)):
            current += gas[i] - cost[i]
            if current < 0:
                current = 0
                answer = i + 1
                
        return answer