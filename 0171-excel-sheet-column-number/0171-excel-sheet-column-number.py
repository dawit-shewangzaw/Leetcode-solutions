class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        power = 1
        for char in reversed(columnTitle):
            result += (ord(char) - ord('A') + 1) * power
            power *= 26
        return result