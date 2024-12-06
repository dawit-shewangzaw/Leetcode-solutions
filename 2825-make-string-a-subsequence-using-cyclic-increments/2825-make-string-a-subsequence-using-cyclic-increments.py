class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0  # Pointers for str1 and str2

        while i < len(str1) and j < len(str2):
            # Check if characters match directly or by cyclic increment
            if str1[i] == str2[j] or chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
                j += 1  # Move pointer in str2 if there's a match
            i += 1  # Always move pointer in str1

        # If we matched all characters of str2, it's a subsequence
        return j == len(str2)
