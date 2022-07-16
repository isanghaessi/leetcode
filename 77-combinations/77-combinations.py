from collections import *

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        return combinations([i for i in range(1, n + 1)], k)