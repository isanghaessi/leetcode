class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        i = 0
        while i < len(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                current = nums[i] + nums[l] + nums[r]
                if current < 0:
                    l += 1
                elif current > 0:
                    r -= 1
                else:
                    answer.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
            num = nums[i]
            while i < len(nums) and nums[i] == num:
                i += 1
        
        return list(answer)
            