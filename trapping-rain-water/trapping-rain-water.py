class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        for i, h in enumerate(height):
            max_left_height = max(height[:i]) if height[:i] else h
            max_right_height = max(height[i + 1:]) if height[i + 1:] else h
            if max_left_height > h and max_right_height > h:
                result += min(max_left_height, max_right_height) - h
        return result