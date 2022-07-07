class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        visited = set()
        nums.sort()
        for i in range(len(nums) - 2):
            num = nums[i]
            if num not in visited:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] > -num:
                        r = r - 1
                    elif nums[l] + nums[r] < - num:
                        l = l + 1
                    else:
                        answer.append((num, nums[l], nums[r]))
                        l = l + 1
                        r = r - 1
            visited.add(num)
        
        return list(set(answer))