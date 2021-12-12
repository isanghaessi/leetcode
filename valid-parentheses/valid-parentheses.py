class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {'(': ')', '[': ']', '{':'}'}
        stack = []
        for _s in s:
            if _s in bracket_dict.keys():
                stack.append(_s)
            elif len(stack) < 1 or bracket_dict[stack.pop()] != _s:
                return False
        return len(stack) < 1