class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        memo = {}
        
        def solve(expr):
            if expr in memo:
                return memo[expr]
            
            res = []
            for i in range(len(expr)):
                char = expr[i]
                if char in "+-*":
                    left_results = solve(expr[:i])
                    right_results = solve(expr[i+1:])
                    
                    for l in left_results:
                        for r in right_results:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)
            
            if not res:
                res.append(int(expr))
            
            memo[expr] = res
            return res

        return solve(expression)