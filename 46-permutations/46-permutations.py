from collections import *

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(numsPath):
            if len(numsPath) >= len(nums):
                
                answer.append(numsPath)
            
            for num in [num for num in nums if num not in numsPath]:
                dfs([*numsPath, num])
        
        answer = []
        for num in nums:
            dfs([num])
        
        return answer