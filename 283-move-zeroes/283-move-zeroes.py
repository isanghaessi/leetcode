class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack = []
        for i in range(len(nums) - 1, -1 , -1):
            if nums[i] == 0:
                nums[i:i + len(stack) + 1] = [*stack[::-1], 0]
            else:
                stack.append(nums[i])
        