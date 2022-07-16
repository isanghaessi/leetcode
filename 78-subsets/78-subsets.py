class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, numsPath, size):
            if (len(numsPath) == size):
                answer.append(numsPath)
                
                return
            for i, num in enumerate(nums):
                dfs(nums[i + 1:], (*numsPath, num), size)
        
        
        answer =[]
        for i in range(len(nums) + 1):
            dfs(tuple(nums), (), i)
        
        return answer