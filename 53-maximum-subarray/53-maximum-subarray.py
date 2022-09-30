class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
            i += 1
        
        return max(nums)