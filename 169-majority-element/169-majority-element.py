class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) < 1:
            
            return None
        if len(nums) == 1:
            
            return nums[0]
        
        halfLen = len(nums) // 2
        l = self.majorityElement(nums[:halfLen])
        r = self.majorityElement(nums[halfLen:])
        
        return [r, l][nums.count(l) > halfLen]