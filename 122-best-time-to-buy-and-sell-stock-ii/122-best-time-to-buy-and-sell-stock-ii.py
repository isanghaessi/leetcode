class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        currentMin = float('inf')
        for price in prices:
            if currentMin < price:
                print(price)
                answer += price - currentMin
            if currentMin != price:
                currentMin = price
        
        return answer