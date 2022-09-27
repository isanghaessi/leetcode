class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binSearch(l, r):
            if l > r:
                
                return -1
            
            m = (l + r) // 2
            if nums[m][1] == target:
                
                return nums[m][0]
            elif nums[m][1] > target:
                
                return binSearch(l, m - 1)
            else:
                
                return binSearch(m + 1, r)
            
            
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        nums = list(enumerate(nums))
        nums = nums[l:] + nums[:l]
        
        return binSearch(0, len(nums) - 1)