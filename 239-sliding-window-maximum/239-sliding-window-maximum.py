import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            
            return nums
        else:
            current = collections.deque()
            answer = []
            for index, num in enumerate(nums):
                while len(current) > 0 and num >= nums[current[-1]]:
                    current.pop()
                current.append(index)
                if index + 1 >= k:
                    answer.append(nums[current[0]])
                if index - current[0] + 1 == k:
                    current.popleft()
            
            return answer