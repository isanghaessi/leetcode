class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        answer = 0
        g.sort()
        s.sort(reverse = True)
        for _s in s:
            while len(g) > 0:
                biggest_child = g.pop()
                if biggest_child <= _s:
                    answer += 1
                    
                    break
        
        return answer