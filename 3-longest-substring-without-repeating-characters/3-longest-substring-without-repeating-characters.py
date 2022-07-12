class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        answer = 0
        left = 0
        for i, c in enumerate(s):
            if c in used and left <= used[c]:
                left = used[c] + 1
            else:
                answer = max(answer, i - left + 1)
            used[c] = i
        
        return answer