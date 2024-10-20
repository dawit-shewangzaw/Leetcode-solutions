class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # Helper function to split the sub-expressions inside parentheses
        def split(expr: str) -> list:
            parts = []
            balance = 0
            curr = []
            for char in expr:
                if char == '(':
                    balance += 1
                if char == ')':
                    balance -= 1
                if char == ',' and balance == 0:
                    parts.append(''.join(curr))
                    curr = []
                else:
                    curr.append(char)
            parts.append(''.join(curr))  # add the last part
            return parts
        
        # The main evaluation function
        def evaluate(expr: str) -> bool:
            if expr == 't':
                return True
            if expr == 'f':
                return False
            if expr[0] == '!':
                # Inversion case
                return not evaluate(expr[2:-1])
            elif expr[0] == '&':
                # AND case
                sub_exprs = split(expr[2:-1])
                return all(evaluate(sub) for sub in sub_exprs)
            elif expr[0] == '|':
                # OR case
                sub_exprs = split(expr[2:-1])
                return any(evaluate(sub) for sub in sub_exprs)
        
        # Start evaluating the full expression
        return evaluate(expression)
