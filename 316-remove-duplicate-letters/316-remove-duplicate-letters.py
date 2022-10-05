from collections import *

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = Counter(s), []
        for _s in s:
            counter[_s] -= 1
            
            if _s in stack:
                
                continue
            
            while len(stack) > 0 and _s < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(_s)
        
        return ''.join(stack)