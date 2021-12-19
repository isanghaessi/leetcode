import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt(x * x + y * y), i) for i, (x, y) in enumerate(points)]
        k_smallest = heapq.nsmallest(k, distances)
    
        return [points[ks[1]] for ks in k_smallest]
        