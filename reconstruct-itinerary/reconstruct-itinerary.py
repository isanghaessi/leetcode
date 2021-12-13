import collections
import copy

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(path, tickets_dict):
            nonlocal answer
            
            if len(answer) > 0:
                
                return
            if len(list(filter(lambda a: len(a) > 0, tickets_dict.values()))) < 1:
                answer = path
            current = path[-1]
            for tdc in tickets_dict[current]:
                pass_tickets_dict = copy.deepcopy(tickets_dict)
                pass_tickets_dict[current].remove(tdc)
                dfs([*path, tdc], pass_tickets_dict)
        
        tickets_dict = collections.defaultdict(list)
        for fr, to in tickets:
            tickets_dict[fr].append(to)
        for fr in tickets_dict:
            tickets_dict[fr].sort()
        answer = []
        dfs(['JFK'], tickets_dict)
        
        return answer