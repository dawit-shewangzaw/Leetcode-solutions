class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Initialize pointers for num1 and num2 from the rightmost side
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        # Loop until both strings are processed and no carry is left
        while i >= 0 or j >= 0 or carry:
            # Get the value of the current digit or 0 if index is out of bounds
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            # Compute the sum of current digits and carry
            total = n1 + n2 + carry
            carry = total // 10  # Compute the carry for the next step
            result.append(str(total % 10))  # Append current digit to the result

            # Move to the next digits
            i -= 1
            j -= 1

        # The result list contains the sum in reverse order
        return ''.join(result[::-1])
