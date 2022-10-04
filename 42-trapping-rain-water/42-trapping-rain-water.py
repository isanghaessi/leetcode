class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        stack = []
        for i in range(len(height)):
            while len(stack) > 0 and height[stack[-1]] < height[i]:
                bottom = height[stack.pop()]
                
                if len(stack) < 1:
                    
                    break
                
                answer += (min(height[stack[-1]], height[i]) - bottom) * (i - stack[-1] - 1)
            stack.append(i)
        
        return answer