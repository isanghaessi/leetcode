import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        left = 0
        right = 1
        while left < right and right <= len(s):
            while right <= len(s) and collections.Counter(s[left:right]).most_common(1)[0][1] < 2:
                answer = max(answer, len(s[left:right]))
                right += 1
            while left < right and collections.Counter(s[left:right]).most_common(1)[0][1] > 1:
                left += 1
        return answer