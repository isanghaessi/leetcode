class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for _s in sorted(set(s)):
            suffix = s[s.index(_s):]
            if set(suffix) == set(s):
                return _s + self.removeDuplicateLetters(suffix.replace(_s, ''))
        
        return ''