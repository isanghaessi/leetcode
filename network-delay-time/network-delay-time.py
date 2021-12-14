import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        times_dict = collections.defaultdict(list)
        for u, v, w in times:
            times_dict[u].append([w, v, u])
        dists = collections.defaultdict(lambda :float('inf'))
        dists['start'] = 0
        hq = [[0, k, 'start']]
        while len(hq) > 0:
            w, v, u = heapq.heappop(hq)
            if dists[v] == float('inf'):
                dists[v] = w
                for nw, nv, nu in times_dict[v]:
                    heapq.heappush(hq, [dists[v] + nw, nv, nu])
                    
        print(dists)
        
        return max(list(dists.values())) if len(list(dists.values())) > n else -1