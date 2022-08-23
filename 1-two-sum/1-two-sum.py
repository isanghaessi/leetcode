class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort(key = lambda a: a[0])
        l, r = 0, len(nums) - 1
        while True:
            current = nums[l][0] + nums[r][0]
            if current < target:
                l += 1
            elif current > target:
                r -= 1
            else:
                
                return (nums[l][1], nums[r][1])