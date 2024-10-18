class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        divisors_sum = 1  # Start with 1 as it's always a divisor
        # Check divisors up to the square root of num
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisors_sum += i
                if i != num // i:  # Add both divisors (i and num // i)
                    divisors_sum += num // i
        
        return divisors_sum == num