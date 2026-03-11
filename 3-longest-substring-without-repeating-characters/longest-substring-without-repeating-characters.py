class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        output = 0
        unique = ""

        if len(set(s)) == 1:
            return 1

        while left <= right and right < len(s):
            if s[right] not in unique:
                unique += s[right]
                right += 1
                output = max(output , len(unique))
            else:
                unique = unique[1:]
                left += 1
                output = max(output , len(unique))

        return output