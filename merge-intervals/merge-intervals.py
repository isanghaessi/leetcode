class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda a: a[0])
        answer = []
        i = 0
        while i < len(intervals):
            fr, to = intervals[i]
            for j in range(i, len(intervals)):
                if intervals[j][0] <= to:
                    to = max(to, intervals[j][1])
                    i = j + 1
                else:
                    
                    break
            answer.append([fr, to])
            
        return answer
                
            