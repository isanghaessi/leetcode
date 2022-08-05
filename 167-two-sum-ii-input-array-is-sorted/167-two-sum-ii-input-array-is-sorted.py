from bisect import *

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        i = 0
        while i < len(numbers):
            iTarget = target - numbers[i]
            j = bisect_left(numbers, iTarget, lo = i + 1)
            if j < len(numbers) and numbers[j] == iTarget :
                
                return (i + 1, j + 1)
            i += 1