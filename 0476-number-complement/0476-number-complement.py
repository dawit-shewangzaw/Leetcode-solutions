class Solution:
    def findComplement(self, num: int) -> int:
        # Step 1: Create a mask with all bits set to 1
        # The mask has the same number of bits as num
        mask = (1 << num.bit_length()) - 1
        
        # Step 2: XOR num with the mask to get the complement
        return num ^ mask
