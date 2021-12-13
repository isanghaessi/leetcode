import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for i in range(len(nums) + 1):
            answer = [*answer, *map(list,itertools.combinations(nums, i))]
        return answer