import functools

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1, *nums[:len(nums) - 1]]
        right = [*nums[1:], 1]
        for i in range(len(nums) - 1):
            left[i + 1] = left[i] * left[i + 1]
            right[len(nums) - i - 2] = right[len(nums) - i - 1] * right[len(nums) - i - 2]
        return [left[i] * right[i] for i in range(len(nums))]