import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        return str(int(''.join(map(str, sorted(nums, key = functools.cmp_to_key(lambda a, b: int(str(b) + str(a)) - int(str(a) + str(b))))))))