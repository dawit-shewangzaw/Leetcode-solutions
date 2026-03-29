class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        last_double_index = 0
        duplicates_count = 0
        max_length = 1 

        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                duplicates_count += 1
                
                if duplicates_count > 1:
                    left = last_double_index
                    duplicates_count = 1
                
                last_double_index = right

            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length