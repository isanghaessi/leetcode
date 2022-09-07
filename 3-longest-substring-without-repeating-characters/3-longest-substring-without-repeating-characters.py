class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        i = 0
        while i < len(s):
            current = s[i]
            while i + 1 < len(s) and s[i + 1] == current:
                i += 1
            j = i
            check = set()
            while j < len(s) and s[j] not in check:
                check.add(s[j])
                j += 1
            answer = max(answer, j - i)
            i += 1
        
        return answer