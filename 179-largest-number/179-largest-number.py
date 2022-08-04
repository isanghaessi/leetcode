from functools import *

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key = cmp_to_key(lambda a, b: int(b + a) - int(a + b)))
        
        return str(int(''.join(nums)))