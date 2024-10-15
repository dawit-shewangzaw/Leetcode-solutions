class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        width_of_last_line = 0

        for char in s:
            width_of_char = widths[ord(char) - ord('a')]
            
            if width_of_last_line + width_of_char > 100:
                lines += 1
                width_of_last_line = width_of_char
            else:
                width_of_last_line += width_of_char

        return [lines, width_of_last_line]
