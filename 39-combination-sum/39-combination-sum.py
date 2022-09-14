class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def find(candidates, path):
            pathSum = sum(path)
            if pathSum > target:
                
                return
            if pathSum == target:
                answer.append(path)
                
                return
            
            for i, candidate in enumerate(candidates):
                find(candidates[i:], [*path, candidate])
        
        answer = []
        find(candidates, [])
        
        return answer