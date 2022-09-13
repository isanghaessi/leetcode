class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def comb(left, current, result):
            if len(current) >= k:
                
                return [*result, current]
            
            if len(left) < 1:
                
                return result
            
            for i, l in enumerate(left):
                result = comb(left[i + 1:], [*current, left[i]], result)
            
            return result
        
        return comb([i for i in range(1, n + 1)], [], [])