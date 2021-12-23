# import collections

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if k == 1:
            
#             return nums
#         else:
#             current = collections.deque(nums[:k])
#             answer = [max(nums[:k])]
#             for i in range(k, len(nums)):
#                 prev = answer[-1]
#                 dropped = current.popleft()
#                 new = nums[i]
#                 current.append(new)
#                 if dropped == prev:
#                     answer.append(max(current))
#                 else:
#                     answer.append(prev if prev > new else new)
                    
#             return answer
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []
        for i in range(len(nums)):
            # the first/left (max) element is out of the current window
            if q and i - q[0] == k:
                q.popleft()
            while q:
                # pop useles elements from last/right of the queue
                if nums[q[-1]] < nums[i]:
                    q.pop()
                else:
                    break
            q.append(i)
            if i >= k-1: # i == k-1 is the beginning of a full window
                result.append(nums[q[0]])
        return result