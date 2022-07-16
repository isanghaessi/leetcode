class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(path):
            sortedPath = tuple(sorted(path))
            if sortedPath in visitedPath:
                
                return
            else:
                visitedPath[tuple(sorted(path))] = True
                
            if sum(path) > target:  
                
                return
            if sum(path) == target:
                answer.append(path)
                
                return
            
            for candidate in candidates:
                dfs((*path, candidate))
        
        
        answer = []
        visitedPath = {}
        dfs(())
        
        return answer