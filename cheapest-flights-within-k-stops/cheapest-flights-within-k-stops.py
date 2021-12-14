import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         flights_dict = collections.defaultdict(list)
#         for fr, to , pr in flights:
#             flights_dict[fr].append([pr, to])
#         hq = [[0, src, 0]]
#         while len(hq) > 0:
#             pr, to, nof = heapq.heappop(hq)
#             if to == dst:
                    
#                 return pr
#             if nof < k + 1:
#                 for npr, nto in flights_dict[to]:
#                     heapq.heappush(hq, [pr + npr, nto, nof + 1])
                    
#         return -1
        prev = [float('inf') for _ in range(n)]
        curr = [float('inf') for _ in range(n)]
        prev[src] = 0
        curr[src] = 0
        count = 0
        
        while count < k+1:
            for f in flights:
                curr[f[1]] = min(prev[f[0]]+f[2], prev[f[1]], curr[f[1]])
            prev, curr = curr, prev
            count += 1
        
        return prev[dst] if prev[dst] < float('inf') else -1