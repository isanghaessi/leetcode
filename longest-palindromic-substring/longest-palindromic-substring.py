import pprint

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        s = ' '.join(list(s))
        result = s[0]
        center = 0
        while center < len(s):
            gap = len(result) // 2
            while center - gap >= 0 and center + gap + 1 <= len(s) and s[center - gap: center + gap + 1] == s[center - gap: center + gap + 1][::-1]:
                if len(result.replace(' ', '')) < len(s[center - gap: center + gap + 1].replace(' ', '')):
                    result = s[center - gap: center + gap + 1]
                gap += 1
            center += 1
        return result.replace(' ', '')