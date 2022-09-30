from collections import *

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        halfNumsLen = len(nums) // 2
        numsCounter = Counter(nums)
        for nc in numsCounter:
            if numsCounter[nc] > halfNumsLen:
                
                return nc