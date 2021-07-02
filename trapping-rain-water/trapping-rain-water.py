class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            
            return 0
        result = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        while left < right:
            if left_max <= right_max:
                left += 1
                if left_max >= height[left]:
                    result += left_max - height[left]
                else:
                    left_max = height[left]
            else:
                right -= 1
                if right_max >= height[right]:
                    result += right_max - height[right]
                else:
                    right_max = height[right]
                    
        return result
                