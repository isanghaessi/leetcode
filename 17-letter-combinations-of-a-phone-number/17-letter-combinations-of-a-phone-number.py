class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(restDigits, pressedAlpha):
            if len(restDigits) < 1:
                answer.append(pressedAlpha)
                
                return;
            currentDigit = restDigits.pop()
            for cda in digitAlphaDict[currentDigit]:
                dfs(restDigits[:], pressedAlpha + cda)
                
                
        if len(digits) == 0:
            
            return []
        
        digitAlphaDict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        answer = []
        dfs(list(digits)[::-1], '')
        
        return answer