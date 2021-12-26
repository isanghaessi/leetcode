import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counter = collections.Counter()
        for right in range(1, len(s) + 1):
            counter[s[right - 1]] += 1
            mc = counter.most_common(1)[0][1]
            if right - left - mc > k:
                counter[s[left]] -= 1
                left += 1
        
        return right - left