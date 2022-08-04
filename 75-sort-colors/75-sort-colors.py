class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
            
            
        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            print(i, left, right, nums)
            if nums[i] == 0:
                swap(i, left)
                left += 1
                i += 1
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
            else:
                i += 1
