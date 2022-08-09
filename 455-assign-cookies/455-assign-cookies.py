from heapq import *

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        answer = 0
        i = len(g) - 1
        while i >= 0 and len(s) > 0:
            if g[i] <= s[-1]:
                s.pop()
                answer += 1
            i -= 1
        
        return answer