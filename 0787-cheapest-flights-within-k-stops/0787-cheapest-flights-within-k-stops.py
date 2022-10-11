# from collections import *

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         flightDict = defaultdict(list)
#         for fr, to, pr in flights:
#             flightDict[fr].append((pr, to))
#         hq = [(0, src, -1)]
#         while len(hq) > 0:
#             price, current, count = heappop(hq)
#             if current == dst:
                
#                 return price
            
#             if count + 1 <= k:
#                 for pr, to in flightDict[current]:
#                     heappush(hq, (price + pr, to, count + 1))
        
#         return -1
import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flights_dict = collections.defaultdict(list)
        for fr, to , pr in flights:
            flights_dict[fr].append([pr, to])
        prices = collections.defaultdict(lambda :float('inf'))
        nofs = collections.defaultdict(int)
        hq = [[0, src, 0]]
        while len(hq) > 0:
            pr, to, nof = heapq.heappop(hq)
            if to == dst:
                    
                return pr
            if (pr < prices[to] or nof < nofs[to]) and nof < k + 1:
                prices[to] = pr
                nofs[to] = nof
                for npr, nto in flights_dict[to]:
                    heapq.heappush(hq, [pr + npr, nto, nof + 1])
                    
        return -1