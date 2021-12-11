import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z^A-Z^0-9]', '', s)
        print(s, s[::-1])
        return s == s[::-1]