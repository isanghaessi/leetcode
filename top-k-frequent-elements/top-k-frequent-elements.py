import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(map(lambda a: a[0], collections.Counter(nums).most_common(k)))