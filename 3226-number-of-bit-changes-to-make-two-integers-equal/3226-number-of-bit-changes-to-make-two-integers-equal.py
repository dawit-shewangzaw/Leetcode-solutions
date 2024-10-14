class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # If k contains bits that are '1' where n has '0', it is impossible
        if k & ~n != 0:
            return -1
        
        # XOR n and k to find where the bits differ
        different_bits = n ^ k
        
        # Count how many '1's are in the result of n ^ k
        return bin(different_bits).count('1')
