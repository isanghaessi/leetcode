class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        for i in range(len(bin(n)) - 2):
            mask = 0b1 << i
            if n & mask:
                answer += 1
        
        return answer
            