class Solution:
    robbed = {}
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:

            return 0
        if len(nums) < 3:

            return max(nums)
        current = ''.join(map(str, nums))
        if current not in self.robbed:
            self.robbed[current] = max([self.rob(nums[:i - 1 if i - 1 >= 0 else 0]) + nums[i] + self.rob(nums[i + 2:]) for i in range(len(nums))])

        return self.robbed[current]            
