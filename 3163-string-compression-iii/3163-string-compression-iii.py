class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        
        while i < len(word):
            count = 1
            # Count consecutive characters, with a max of 9
            while i + count < len(word) and word[i] == word[i + count] and count < 9:
                count += 1
            # Append count and character to the result
            comp += f"{count}{word[i]}"
            # Move to the next character sequence
            i += count
            
        return comp
