class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def findLongerString(i, j):
            if j + 1 >= len(s):
                
                return (i, j)
            alphaSet = set(s[i:j + 1])
            k = j
            for alpha in alphaSet:
                l = j + 1
                while alpha in s[l:]:
                    l = l + 1
                k = max(k, l - 1)
            if j < k:
                
                return findLongerString(i, k)
            
            return (i, j)
        
        
        result = []
        
        i = 0
        while i < len(s):
            i, newI = findLongerString(i, i)
            result.append(newI - i + 1)
            i = newI + 1
        
        return result