class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda a: a[0])
        i = 0
        while i < len(intervals):
            current = intervals[i]
            while i + 1 < len(intervals) and current[1] >= intervals[i + 1][0]:
                current[1] = max(current[1], intervals[i + 1][1])
                del intervals[i + 1]
            i += 1
        
        return intervals