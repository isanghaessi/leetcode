from collections import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counterDict = defaultdict(list)
        for s in strs:
            counterDict[tuple(sorted(Counter(s).items()))].append(s)
            
        return counterDict.values()