from bisect import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            for _m in m:
                if _m == target:
                    
                    return True
        
        return False