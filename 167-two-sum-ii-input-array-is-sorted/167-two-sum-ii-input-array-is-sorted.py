from bisect import *

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        i = 0
        while i < len(numbers):
            findTarget = target - numbers[i]
            foundIndex = bisect_left(numbers, findTarget, lo = i + 1)
            if foundIndex < len(numbers) and numbers[foundIndex] == findTarget:
                
                return (i + 1, foundIndex + 1)
            i += 1