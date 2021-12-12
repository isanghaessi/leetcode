import re

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for alpha in sorted(set(s)):
            suffix = s[s.index(alpha):]
            if set(s) == set(suffix):
                return alpha + self.removeDuplicateLetters(suffix.replace(alpha, ''))
        return ''