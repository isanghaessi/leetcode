from collections import *

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flightDict = defaultdict(list)
        for fr, to, pr in flights:
            flightDict[fr].append((pr, to))
        hq = [(0, src, -1)]
        countDict = defaultdict(lambda : float('inf'))
        while len(hq) > 0:
            price, current, count = heappop(hq)
            if count > k or count >= countDict[current]:
                
                continue
            if current == dst:
                
                return price
            
            countDict[current] = count
            for pr, to in flightDict[current]:
                heappush(hq, (price + pr, to, count + 1))
        
        return -1