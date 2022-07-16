class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(nums, numsPath):
            if len(numsPath) == k:
                answer.append(numsPath)
                
                return
            for i, num in enumerate(nums):
                dfs(nums[i + 1:], (*numsPath, num))
        
        
        answer = []
        dfs([i for i in range(1, n + 1)], ())
        
        return answer