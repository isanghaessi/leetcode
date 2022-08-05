class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binSearch(nums, left, right, target):
            if left > right:
                
                return - 1
            
            index = (left + right) // 2
            if nums[index] < target:
                
                return binSearch(nums, index + 1, right, target)
            elif nums[index] > target:
                
                return binSearch(nums, left, index - 1, target)
            else:
                
                return index
        
        
        i = 0
        while i < len(numbers):
            j = binSearch(numbers[i + 1:], 0, len(numbers) - i - 2, target - numbers[i])
            if j >= 0:
                
                return (i + 1, i + j + 2)
            i += 1