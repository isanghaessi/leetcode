class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binSearch(left, right):
            if left > right:
                
                return -1
            
            index = (left + right) // 2
            answer = -1
            if nums[index] == target:
                answer = index
            elif nums[index] < target:
                answer = binSearch(index + 1, right)
                if answer < 0:
                    answer = binSearch(left, index - 1)
            else:
                answer = binSearch(left, index - 1)
                if answer < 0:
                    answer = binSearch(index + 1, right)
            
            return answer
        
        
        return binSearch(0, len(nums) - 1)