class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            
            return 0
        minNum = min(nums)
        maxNum = max(nums)
        numDict = {}
        for num in nums:
            numDict[num] = True
        result = consecutive = 0
        for num in range(minNum, maxNum + 1):
            if num in numDict:
                consecutive = consecutive + 1
                del numDict[num]
            else:
                consecutive = 0
                if len(numDict.keys()) <= result:
                    
                    break   
            result = max(result, consecutive)
        result = max(result, consecutive)    
        
        return result