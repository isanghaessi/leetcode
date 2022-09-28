class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        if len(x) < len(y):
            x = ('0' * (len(y) - len(x))) + x
        if len(y) < len(x):
            y = ('0' * (len(x) - len(y))) + y
        answer = 0
        i = 0
        while i < len(x) and len(y):
            if x[i] != y[i]:
                answer += 1
            i += 1
        
        return answer
        