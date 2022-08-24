class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        stack = []
        for i in range(len(height)):
            while len(stack) > 0 and height[stack[-1]] < height[i]:
                left = stack.pop()
                if len(stack) < 1:
                    
                    break
                
                distance = i - stack[-1] - 1
                water = min(height[i], height[stack[-1]]) - height[left]
                answer += distance * water
            stack.append(i)
        
        return answer