from collections import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = defaultdict(list)
        for i, num in enumerate(nums):
            numsDict[num].append(i)
        for num in list(numsDict.keys()):
            if (len(numsDict[target - num]) > 0 and target - num != num) or (len(numsDict[target - num]) > 1 and target - num == num):
                
                return (numsDict[num].pop(), numsDict[target - num].pop())