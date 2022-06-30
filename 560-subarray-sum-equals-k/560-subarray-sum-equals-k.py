class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:

		result=0
		prefixSum=0
		prefixDictionary={0:1}

		for num in nums:
			prefixSum = prefixSum + num

			if prefixSum - k in prefixDictionary:
				result = result + prefixDictionary[prefixSum - k]

			if prefixSum not in prefixDictionary:
				prefixDictionary[prefixSum] = 1
			else:
				prefixDictionary[prefixSum] = prefixDictionary[prefixSum] + 1

		return result