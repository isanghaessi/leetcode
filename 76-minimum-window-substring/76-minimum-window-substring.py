from collections import *

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def dictIn(d, td):
            for _td in td:
                if _td not in d or d[_td] < td[_td]:
                    
                    return False
            
            return True
        
        
        answer = ''
        l = 0
        r = 1
        targetDict = Counter(t)
        currentDict = defaultdict(int)
        currentDict[s[l]] += 1
        queue = deque([l])
        while len(queue) > 0:
            nextL = queue.popleft()
            for i in range(l, nextL):
                currentDict[s[i]] -= 1
            l = nextL
            while r < len(s) and not dictIn(currentDict, targetDict):
                currentDict[s[r]] += 1
                if s[r] in targetDict:
                    queue.append(r)
                r += 1
            if dictIn(currentDict, targetDict):
                answer = min(answer, s[l:r], key = len) if answer != '' else s[l:r]
                
        return answer
