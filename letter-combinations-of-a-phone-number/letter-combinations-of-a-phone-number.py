import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(string, rest):
            nonlocal answer
            
            current = rest[0]
            rest = rest[1:]
            for adc in alpha_dict[current]:
                if len(rest) < 1:
                    answer.add(string + adc)
                else:
                    for i, r in enumerate(rest):
                        dfs(string + adc, rest)
            
        
        if len(digits) < 1:
            return []
        
        alpha_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        answer = set()
        dfs('', digits)
        
        return answer