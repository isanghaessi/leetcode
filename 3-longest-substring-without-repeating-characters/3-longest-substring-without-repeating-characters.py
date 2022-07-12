class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        for i in range(len(s)):
            alphaDict = {}
            count = 0
            for j in range(i, len(s)):
                if s[j] not in alphaDict:
                    alphaDict[s[j]] = True
                    count += 1
                else:
                    
                    break
            answer = max(answer, count)
        
        return answer