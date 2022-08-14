class Solution:
    dp = {}
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            
            return max(nums)
        
        nums = tuple(nums)
        if nums in self.dp:
            
            return self.dp[nums]
        
        self.dp[nums] = max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        
        return self.dp[nums]