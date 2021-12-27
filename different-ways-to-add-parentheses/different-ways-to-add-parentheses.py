class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        print(expression)
        if not any(map(lambda a: a in expression, '+-*')):
        
            return [expression]
        answer = []
        i = 0
        while i < len(expression):
            if expression[i] in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for l in left:
                    for r in right:
                        answer.append(str(eval(l + expression[i] + r)))
            i += 1
            
        return answer