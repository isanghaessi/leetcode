class Solution:
    def minPartitions(self, n: str) -> int:
        def dfs(numberString, count):
            if int(numberString) == 0:
                
                return count
            newNumberList = []
            for digitString in numberString:
                intDigit = int(digitString)
                if intDigit > 0:
                    newNumberList.append(str(intDigit - 1))
                else:
                    newNumberList.append('0')
            
            return dfs(''.join(newNumberList), count + 1)
        
        
        return dfs(n, 0)