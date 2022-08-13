class Solution:
    operations = ['+', '-', '*', '/']
    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, op, right):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            
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
                