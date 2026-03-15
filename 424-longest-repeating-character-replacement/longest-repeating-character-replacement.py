class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {} # Hash map to store character frequencies in the window
        max_f = 0  # Frequency of the most common character in the window
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # 1. Update the frequency of the current character
            char = s[right]
            count[char] = count.get(char, 0) + 1
            
            # 2. Update the most frequent character count in the current window
            max_f = max(max_f, count[char])
            
            # 3. Check if the window is valid
            while (right - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1
            
            # 4. Update the maximum length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length