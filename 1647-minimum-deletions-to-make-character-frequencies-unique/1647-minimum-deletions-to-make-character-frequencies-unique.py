from collections import *

class Solution:
    def minDeletions(self, s: str) -> int:
        counterValues = sorted(list(dict(Counter(s)).values()))
        result = 0
        for i in range(len(counterValues) - 1):
            if counterValues[i] == counterValues[i + 1]:
                counterValues[i] = counterValues[i] - 1
                result = result + 1
                j = i
                while j >= 0 and j - 1 >= 0 and counterValues[j - 1] > 0 and counterValues[j - 1] == counterValues[j]:
                    j = j - 1
                    counterValues[j] = counterValues[j] - 1
                    result = result + 1
        
        return result