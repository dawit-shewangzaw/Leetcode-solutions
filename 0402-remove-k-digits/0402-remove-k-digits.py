class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        # Iterate over each digit in num
        for digit in num:
            # Remove the last element in stack if it's larger than current digit and we still have k removals left
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If we still have digits to remove, remove them from the end
        stack = stack[:-k] if k else stack
        
        # Convert stack back to string and remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        # Return result or '0' if result is empty
        return result if result else '0'
