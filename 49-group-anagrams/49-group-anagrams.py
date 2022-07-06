from collections import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answerDict = defaultdict(list)
        for s in strs:
            answerDict[tuple(sorted(s))].append(s)
            
        return answerDict.values()