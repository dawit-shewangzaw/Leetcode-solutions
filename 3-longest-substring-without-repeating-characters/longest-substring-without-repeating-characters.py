class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_value = set()
        left = 0
        output = 0

        for right in range(len(s)):
            while s[right] in unique_value:
                unique_value.remove(s[left])
                left += 1
            
            unique_value.add(s[right])
            output = max(output , right - left + 1)

        return output
       

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         left = 0
#         right = 0
#         output = 0
#         unique = ""
#         adict = defaultdict(int)
        
#         for right in range(len(s)):
#             adict[s[right]] += 1

#             while left < len(s) and len(adict) != (right - left + 1):
#                 adict[s[right]] -= 1
#                 if adict[s[left]] == 0:
#                     del adict[s[left]]
#                 left += 1
#             output = max(output , right - left + 1)
        
#         return output


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         left = 0
#         right = 0
#         output = 0
#         unique = ""

#         if len(set(s)) == 1:
#             return 1

#         while left <= right and right < len(s):
#             if s[right] not in unique:
#                 unique += s[right]
#                 right += 1
#                 output = max(output , len(unique))
#             else:
#                 unique = unique[1:]
#                 left += 1
#                 output = max(output , len(unique))

#         return output