class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, numsPath):
            answer.append(numsPath)
            
            if (len(nums) < 1):
                
                return
            
            for i, num in enumerate(nums):
                dfs(nums[i + 1:], (*numsPath, num))
        
        
        answer = []
        dfs(tuple(nums), ())
        
        return answer