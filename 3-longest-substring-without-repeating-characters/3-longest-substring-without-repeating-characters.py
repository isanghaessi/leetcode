class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        alphaDict = {}
        left = 0
        while left < len(s):
            right = left
            while right < len(s):
                if s[right] in alphaDict:
                    answer = max(answer, right - left)
                    left = alphaDict[s[right]] + 1
                    alphaDict = {}
                    
                    break
                alphaDict[s[right]] = right
                right += 1
            if right >= len(s):
                answer = max(answer, right - left)
                
                break
            
        return answer