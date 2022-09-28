from collections import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        dp = {}
        for num in nums:
            if num in dp:
                answer -= num
            else:
                answer += num
                dp[num] = True
        
        return answer
            