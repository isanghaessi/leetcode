class Solution:
    def isValid(self, s: str) -> bool:
        bracketDict = {')': '(', ']': '[', '}': '{'}
        stack = []
        for _s in s:
            if _s not in bracketDict:
                stack.append(_s)
            elif len(stack) < 1 or stack.pop() != bracketDict[_s]:
                
                return False
        
        return len(stack) == 0