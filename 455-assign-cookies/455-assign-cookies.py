from bisect import *

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        answer = 0
        for _s in s:
            if bisect_right(g, _s) > answer:
                answer += 1
                
        return answer