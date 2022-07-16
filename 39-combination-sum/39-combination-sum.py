class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, path):   
            if sum(path) > target:
                
                return
            if sum(path) == target:
                answer.append(path)
                
                return
            
            for i, candidate in enumerate(candidates):
                dfs(candidates[i:], (*path, candidate))
        
        
        answer = []
        dfs(candidates, ())
        
        return answer