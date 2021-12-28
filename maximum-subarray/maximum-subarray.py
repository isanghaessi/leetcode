import functools

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [float('-inf')]
        for i in range(len(nums)):
            sums.append(sums[i] + nums[i] if sums[i] > 0 else nums[i])
            
        return max(sums)