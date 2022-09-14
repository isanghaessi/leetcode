class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def find(candidates, path):
            pathSum = sum(path)
            if pathSum > target:
                
                return
            if pathSum == target:
                path.sort()
                if tuple(path) not in answer:
                    answer.append(tuple(path))
                
                return
            
            for i, candidate in enumerate(candidates):
                path.append(candidate)
                find(candidates[i:], path)
                path.remove(candidate)
        
        answer = []
        find(candidates, [])
        
        return answer