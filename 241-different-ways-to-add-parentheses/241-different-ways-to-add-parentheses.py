class Solution:
    operations = ['+', '-', '*', '/']
    dp = {}
    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, op, right):
            results = []
            for l in left:
                for r in right:
                    expression = str(l) + op + str(r)
                    if expression not in self.dp:
                        self.dp[expression] = eval(expression)
                    results.append(self.dp[expression])
            
            return results
        
        
        if expression.isdigit():
            
            return [int(expression)]
        
        answer = []
        for i, e in enumerate(expression):
            if e in self.operations:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                answer.extend(compute(left, e, right))
        
        return answer
                