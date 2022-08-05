class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binSearch(nums, left, right, target):
            if left > right:
                
                return -1
            
            index = (left + right) // 2
            if nums[index] == target:
                
                return index
            elif nums[index] < target:
                
                return binSearch(nums, index + 1, right, target)
            else:
                
                return binSearch(nums, left, index - 1, target)
        
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        nums = nums1 if len(nums1) < len(nums2) else nums2
        targetNums = nums1 if nums == nums2 else nums2
        answer = []
        for num in nums:
            if num not in answer:
                index = binSearch(targetNums, 0, len(targetNums) - 1, num)
                if index >= 0:
                    answer.append(num)
        
        return answer