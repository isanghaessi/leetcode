class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        l, r = 0, len(height) - 1
        while l < r:
            answer = max(answer, min(height[l], height[r]) * abs(l - r))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return answer