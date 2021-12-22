import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            right_numbers = numbers[i + 1:]
            found = bisect.bisect_left(right_numbers, target - numbers[i])
            if 0 <= found and found < len(right_numbers) \
                and right_numbers[found] == target - numbers[i]:
                
                return [i + 1, i + found + 2]
