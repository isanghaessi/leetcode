import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        counts = collections.defaultdict(int)
        hq = [(0, src, 0)]
        for f, t, p in flights:
            graph[f][t] = p
        for i in range(n):
            counts[i] = k + 1
        while len(hq) > 0 :
            price, city, count = heapq.heappop(hq)
            if city == dst:

                return price
            if counts[city] >= count and count + 1 <= k + 1:
                counts[city] = count
                for t, p in graph[city].items():
                    heapq.heappush(hq, (price + p, t, count + 1))

        return -1