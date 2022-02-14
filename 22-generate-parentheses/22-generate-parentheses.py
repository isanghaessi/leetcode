import copy

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(path, rest):
            if rest['('] == 0 and rest[')'] == 0:
                answer.append(path)
                
                return
            if rest['('] > 0:
                leftRest = copy.deepcopy(rest)
                leftRest['('] -= 1
                dfs(path + '(', leftRest)
            if rest[')'] > 0:
                rightRest = copy.deepcopy(rest)
                rightRest[')'] -= 1
                if rest['('] < rest[')']:
                    dfs(path + ')', rightRest)
        
        brackets = {'(': n, ')': n}
        answer = []
        dfs('', brackets)
        
        return answer