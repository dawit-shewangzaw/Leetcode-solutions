class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        hex_str = ""
        
        if num < 0:
            num += 2 ** 32

        while num > 0:
            hex_str = hex_chars[num % 16] + hex_str
            num //= 16

        return hex_str
