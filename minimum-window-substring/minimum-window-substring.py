import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer = ''
        counter = collections.Counter(t)
        missing = len(set(t))
        i = 0
        for j, _s in enumerate(s):
            if _s in counter.keys():
                counter[_s] -= 1
                if counter[_s] == 0:
                    missing -= 1
            while missing == 0:
                answer = answer if len(answer) > 0 and len(answer) < j - i + 1 else s[i:j + 1]
                if s[i] in counter.keys():
                    counter[s[i]] += 1
                    if counter[s[i]] > 0:
                        missing += 1
                i += 1
        
        return answer