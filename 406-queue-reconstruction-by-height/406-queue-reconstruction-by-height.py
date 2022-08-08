from collections import *

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        answer = []
        for h, k in sorted(people, key = lambda a: (-a[0], a[1])):
            i = 0
            count = 0
            while i < len(answer) and count < k:
                if answer[i][0] >= h:
                    count += 1
                i += 1
            answer.insert(i, (h, k))
        
        return answer