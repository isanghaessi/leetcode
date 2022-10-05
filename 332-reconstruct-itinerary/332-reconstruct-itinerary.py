from collections import *

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
        
        graph = defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
        route = []
        dfs('JFK')
        
        return route[::-1]