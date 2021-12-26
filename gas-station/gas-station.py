class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            
            return -1
        answer = 0
        current = 0
        for i in range(len(gas)):
            calc_cost = gas[i] - cost[i]
            if current + calc_cost < 0:
                current = 0
                answer = i + 1
            else:
                current += calc_cost
            
        return answer