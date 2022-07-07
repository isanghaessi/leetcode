from collections import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = defaultdict(list)
        for i, num in enumerate(nums):
            numsDict[num].append(i)
        for num in list(numsDict.keys()):
            leftI = numsDict[num].pop()
            if len(numsDict[target - num]) > 0:
                
                return (leftI, numsDict[target - num].pop())