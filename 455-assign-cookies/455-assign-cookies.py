from heapq import *

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        answer = 0
        while len(g) > 0 and len(s) > 0:
            if g.pop() <= s[-1]:
                s.pop()
                answer += 1
        
        return answer