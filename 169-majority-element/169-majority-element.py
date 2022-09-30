from collections import *

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numDict = defaultdict(int)
        halfNumsLen = len(nums) // 2
        for num in nums:
            numDict[num] += 1
            if numDict[num] > halfNumsLen:
                
                return num