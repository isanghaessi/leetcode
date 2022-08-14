class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefixSum = []
        currentSum = 0
        for num in nums:
            currentSum += num
            prefixSum.append(currentSum)
        answer = float('-inf')
        currentMin = float('inf')
        i = 0
        while i < len(prefixSum):
            answer = max(answer, prefixSum[i], prefixSum[i] - currentMin)
            currentMin = min(currentMin, prefixSum[i])
            i += 1
            
        return answer