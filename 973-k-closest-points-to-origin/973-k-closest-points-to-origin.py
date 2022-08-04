from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        return [mc[1] for mc in nsmallest(k, [((x * x) + (y * y), (x, y)) for x, y in points])]