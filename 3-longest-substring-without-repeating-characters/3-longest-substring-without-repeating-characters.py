class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        alphas = {}
        left = right = 0
        while right < len(s):
            current = s[right]
            if current not in alphas:
                alphas[current] = right
                answer = max(answer, right - left + 1)
            else:
                i = left
                while i < alphas[current]:
                    del alphas[s[i]]
                    i += 1
                left = alphas[current] + 1
                alphas[current] = right
            right += 1
        
        return answer