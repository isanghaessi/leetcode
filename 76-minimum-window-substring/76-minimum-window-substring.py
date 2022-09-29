# from collections import *

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         def dictIn(d, td):
#             for _td in td:
#                 if _td not in d or d[_td] < td[_td]:
                    
#                     return False
            
#             return True
        
        
#         answer = ''
#         l = 0
#         r = 1
#         targetDict = Counter(t)
#         currentDict = defaultdict(int)
#         currentDict[s[l]] += 1
#         queue = deque([l])
#         while len(queue) > 0:
#             nextL = queue.popleft()
#             for i in range(l, nextL):
#                 currentDict[s[i]] -= 1
#             l = nextL
#             while r < len(s) and not dictIn(currentDict, targetDict):
#                 currentDict[s[r]] += 1
#                 if s[r] in targetDict:
#                     queue.append(r)
#                 r += 1
#             if dictIn(currentDict, targetDict):
#                 answer = min(answer, s[l:r], key = len) if answer != '' else s[l:r]
                
#         return answer
from collections import *

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(counter):
            for ct in counterT:
                if counter[ct] < counterT[ct]:
                    
                    return False
            
            return True
        
        
        answer = s
        l, r = 0, 0
        counterT = Counter(t)
        currentCounter = defaultdict(lambda : 0)
        while r < len(s) and l <= r:
            while r < len(s) and not check(currentCounter):
                currentCounter[s[r]] += 1
                r += 1
            while l <= r and check(currentCounter):
                currentCounter[s[l]] -= 1
                l += 1
            answer = min(answer, s[l - 1:r], key = len)
        
        return answer if check(Counter(answer)) else ''