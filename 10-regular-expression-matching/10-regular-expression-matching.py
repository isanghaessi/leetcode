import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        return s in re.compile(p).findall(s)