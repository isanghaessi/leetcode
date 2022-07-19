from collections import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodeDict = defaultdict(list)
        for f, t, v in times:
            nodeDict[f].append((v, t))
        fastTimeDict = {}
        queue = [(0, k)]
        while len(queue) > 0:
            time, node = heappop(queue)
            if node not in fastTimeDict:
                fastTimeDict[node] = time
                for _time, _node in nodeDict[node]:
                    heappush(queue, (time + _time, _node))
        
        for i in range(1, n + 1):
            if i not in fastTimeDict:
                
                return -1
        
        return max(fastTimeDict.values())
