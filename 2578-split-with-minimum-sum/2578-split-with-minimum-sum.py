class Solution:
    def splitNum(self, num: int) -> int:
        # Convert the number to a list of digits
        digits = list(map(int, str(num)))

        # Sort the digits
        digits.sort()

        # Initialize num1 and num2 as strings
        num1, num2 = "", ""

        # Distribute the digits alternately to num1 and num2
        for i, digit in enumerate(digits):
            if i % 2 == 0:
                num1 += str(digit)
            else:
                num2 += str(digit)

        # Convert num1 and num2 to integers and return their sum
        return int(num1) + int(num2)
