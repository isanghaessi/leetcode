from collections import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        for num in nums:
            dp[num] += 1
        for dpKey in dp:
            if dp[dpKey] == 1:
                
                return dpKey