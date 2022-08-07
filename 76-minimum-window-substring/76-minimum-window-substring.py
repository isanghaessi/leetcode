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
        counterT = dict(Counter(t))
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