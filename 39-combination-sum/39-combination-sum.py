class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def find(path):
            pathSum = sum(path)
            if pathSum > target:
                
                return
            if pathSum == target:
                path.sort()
                if tuple(path) not in answer:
                    answer.append(tuple(path))
                
                return
            
            for candidate in candidates:
                path.append(candidate)
                find(path)
                path.remove(candidate)
        
        answer = []
        find([])
        
        return answer