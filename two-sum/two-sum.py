class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, ni in enumerate(nums):
            for j, nj in enumerate(nums[i+1:]):
                if ni + nj == target:
                    return [i, i + j + 1]