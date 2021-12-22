class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        return list(set([num1 for num1 in nums1 if num1 in nums2]))