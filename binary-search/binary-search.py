class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bisect(left, right):
            mid = (left + right) // 2
            if left <= right:
                if nums[mid] < target:
                    
                    return bisect(mid + 1, right)
                elif nums[mid] == target:

                    return mid
                else:
                    
                    return bisect(left, mid - 1)
            else:
                
                return -1
                
        nums.sort()
        
        return bisect(0, len(nums) - 1)