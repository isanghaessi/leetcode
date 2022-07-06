class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''
        maxLR = 0
        s = ' '.join(s)
        for i in range(len(s)):
            l, r = i - maxLR, i + maxLR
            while l >= 0 and r < len(s):
                currentS = s[l:r + 1]
                if currentS != currentS[::-1]:
                    
                    break
                if len(''.join([a for a in answer if a != ' '])) < len(''.join([cs for cs in currentS if cs != ' '])):
                    maxLR = i - l
                    answer = currentS
                l = l - 1
                r = r + 1
        
        return ''.join([a for a in answer if a != ' '])