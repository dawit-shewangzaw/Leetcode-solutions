class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        last = {int(x): i for i, x in enumerate(num_str)}  # Record the last occurrence of each digit
        
        for i, digit in enumerate(num_str):
            for d in range(9, int(digit), -1):  # Check for a larger digit to swap with
                if last.get(d, -1) > i:  # If a larger digit exists and appears later
                    # Swap the current digit with the larger one
                    num_str[i], num_str[last[d]] = num_str[last[d]], num_str[i]
                    return int("".join(num_str))  # Return the maximum number after the swap
        
        return num  # Return the original number if no swap can increase its value
