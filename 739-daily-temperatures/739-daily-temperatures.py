class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        stack = []
        i = 0
        while i < len(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                dayIndex = stack.pop()
                answer[dayIndex] = i - dayIndex
            stack.append(i)
            i += 1
            
        return answer