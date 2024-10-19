class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Extract the least significant bit from n
            bit = n & 1
            # Left shift the result and add the extracted bit
            result = (result << 1) | bit
            # Right shift n to get the next bit in the next iteration
            n >>= 1
        return result
