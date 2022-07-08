class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] + nums[:]
        for i in range(len(nums) - 1):
            left[i + 1] *= left[i]
        del left[-1]
        right = nums[:] + [1]
        for i in range(len(nums) - 1, 0, -1):
            right[i - 1] *= right[i]
        del right[0]
        
        return [left[i] * right[i] for i in range(len(nums))]