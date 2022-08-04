class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        ones = []
        twos = []
        for num in nums:
            if num == 0:
                zeros.append(num)
            elif num == 1:
                ones.append(num)
            else:
                twos.append(num)
        numsLen = len(nums)
        for zero in zeros[::-1]:
            nums.append(zero)
        for one in ones[::-1]:
            nums.append(one)
        for two in twos[::-1]:
            nums.append(two)
        for _ in range(numsLen):
            nums.pop(0)