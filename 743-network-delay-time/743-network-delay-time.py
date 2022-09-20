from collections import *
from heapq import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def checkAllVisited():
            for i in range(1, n + 1):
                if dist[i] == float('inf'):

                    return False
                
            return True
            
            
        nodeDict = defaultdict(list)
        for fr, to, di in times:
            nodeDict[fr].append((to, di))
        dist = defaultdict(lambda : float('inf'))
        hq = [(0, k)]
        while len(hq) > 0 and not checkAllVisited():
            di, current = heappop(hq)
            if dist[current] != float('inf'):
                
                continue
                
            dist[current] = min(dist[current], di)
            for to, d in nodeDict[current]:
                heappush(hq, (dist[current] + d, to))
        
        return max(dist.values()) if checkAllVisited() else -1