class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binSearch(left, right, target):
            if left > right:
                
                return - 1
            
            index = (left + right) // 2
            if numbers[index] < target:
                
                return binSearch(index + 1, right, target)
            elif numbers[index] > target:
                
                return binSearch(left, index - 1, target)
            else:
                
                return index
        
        
        i = 0
        while i < len(numbers):
            j = binSearch(i + 1, len(numbers) - 1, target - numbers[i])
            if j >= 0:
                
                return (i + 1, j + 1)
            i += 1