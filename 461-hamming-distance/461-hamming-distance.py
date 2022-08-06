class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        answer = 0
        xor = x ^ y
        for i in range(len(max(bin(x), bin(y), key = len)) - 2):
            pivot = 0b1 << i
            if xor & pivot:
                answer += 1
        
        return answer