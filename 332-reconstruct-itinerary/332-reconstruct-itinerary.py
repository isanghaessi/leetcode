from collections import *

class Solution:
    answer = []
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def fly(current, count, path):
            if len(self.answer) > 0:
                
                return
            
            if count == flyCount:
                self.answer = path
                
                return
            
            for i in range(len(ticketDict[current])):
                rest = []
                for _ in range(i):
                    rest.append(heappop(ticketDict[current]))
                currentNext = heappop(ticketDict[current])
                for r in rest:
                    heappush(ticketDict[current], r)
                fly(currentNext, count + 1, [*path, currentNext])
                heappush(ticketDict[current], currentNext)
        
        
        ticketDict = defaultdict(list)
        flyCount = 0
        for fr, to in tickets:
            heappush(ticketDict[fr], to)
            flyCount += 1
        fly('JFK', 0, [])
        
        return ['JFK'] + self.answer