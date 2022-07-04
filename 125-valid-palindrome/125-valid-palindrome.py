class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        for _s in s:
            if _s.isalpha() or _s.isdigit():
                newS = newS + _s.lower()
        
        return newS == newS[::-1]