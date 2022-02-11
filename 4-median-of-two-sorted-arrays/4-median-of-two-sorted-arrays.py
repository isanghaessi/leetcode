import collections

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = collections.deque(nums1)
        nums2 = collections.deque(nums2)
        nums = []
        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] < nums2[0]:
                nums.append(nums1.popleft())
            else:
                nums.append(nums2.popleft())
        leftNums = nums1 if len(nums1) > 0 else nums2
        while len(leftNums) > 0:
            nums.append(leftNums.popleft())
        if len(nums) % 2 == 0:
            left, right = len(nums) // 2 - 1, len(nums) // 2
            
            return (nums[left] + nums[right]) / 2
        else:
            
            return nums[len(nums) // 2]