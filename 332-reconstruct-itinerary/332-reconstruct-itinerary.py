from collections import *

class Solution:
    answer = None
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(departure, path):
            if self.answer:
                
                return
            if len([tv for tv in ticketDict.values() if len(tv) > 0]) == 0:
                self.answer = (*path, departure)
                
                return
            for tdd in tuple(ticketDict[departure]):
                ticketDict[departure].remove(tdd)
                dfs(tdd, (*path, departure))
                ticketDict[departure].append(tdd)
                ticketDict[departure].sort()
            
        
        ticketDict = defaultdict(list)
        for departure, arrival in tickets:
            ticketDict[departure].append(arrival)
        for td in ticketDict:
            ticketDict[td].sort()
            
        dfs('JFK', ())
        
        return self.answer