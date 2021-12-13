import itertools

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(current):
            current_sum = sum(current)
            if current_sum > target:
                
                return
            elif current_sum == target:
                answer.add(tuple(sorted(current)))
            else:
                for candidate in candidates:
                    dfs([*current, candidate])
            
        
        answer = set()
        dfs([])
        return list(map(list, answer))