from bisect import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrixSet = set()
        for m in matrix:
            for _m in m:
                matrixSet.add(_m)
        
        return target in matrixSet