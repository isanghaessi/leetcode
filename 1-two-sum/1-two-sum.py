class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = list(enumerate(nums))
        nums.sort(key = lambda a:a[1])
        l, r = 0, len(nums) - 1
        while True:
            sumLR = nums[l][1] + nums[r][1]
            if sumLR < target:
                l = l + 1
            elif sumLR > target:
                r = r - 1
            else:
                
                return (nums[l][0], nums[r][0])
