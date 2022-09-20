from collections import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodeDict = defaultdict(list)
        for fr, to, di in times:
            nodeDict[fr].append((to, di))
        dist = defaultdict(lambda : float('inf'))
        hq = [(0, k)]
        while len(hq) > 0:
            di, current = heappop(hq)
            if dist[current] != float('inf'):
                
                continue
                
            dist[current] = di
            for to, d in nodeDict[current]:
                heappush(hq, (dist[current] + d, to))
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                
                return - 1
        
        return max(dist.values())