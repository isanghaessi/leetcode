from collections import *

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def checkPrefix(binStr, prefix):
            
            return binStr[:len(prefix)] == prefix
        
        
        
        data = deque(data)
        while len(data) > 0:
            binStr = bin(data.popleft())[2:]
            while len(binStr) < 8:
                binStr = '0' + binStr
            if binStr[0] == '1':
                prefix = ''
                i = 0
                while i < len(binStr) and binStr[i] == '1':
                    prefix += '1'
                    i += 1
                prefix += '0'
                prefixCount = prefix.count('1')
                if prefixCount < 2 or prefixCount > 4:
                    
                    return False
                for j in range(prefixCount - 1):
                    if len(data) < 1:
                        
                        return False
                    nextBinStr = bin(data.popleft())[2:]
                    while len(nextBinStr) < 8:
                        nextBinStr = '0' + nextBinStr
                    if not checkPrefix(nextBinStr, '10'):
                        
                        return False
        
        return True
                    