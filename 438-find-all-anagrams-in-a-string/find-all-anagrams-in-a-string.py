class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        output = []
        p_count = Counter(p)
        window = Counter()
        p_length = len(p)
        left = 0

        for right in range(len(s)):
            window[s[right]] += 1
            
            if right >= p_length:
                
                if window[s[right - p_length]] == 1:
                    del window[s[right - p_length]]
                else:
                    window[s[right - p_length]] -= 1

            if window == p_count:
                output.append(right - p_length + 1)
        return output

# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         s_len, p_len = len(s), len(p)
        
#         if s_len < p_len:
#             return []

#         p_count = Counter(p)
#         s_count = Counter(s[:p_len]) # Initialize window with first chunk
#         output = []
#         print("s_count " + str(s_count) )

#         if s_count == p_count:
#             output.append(0)
#         print("output " + str(output))
        
#         for i in range(p_len, s_len):
#             # Add the new character on the right
#             s_count[s[i]] += 1
            
#             left_char = s[i - p_len]
#             s_count[left_char] -= 1
            
#             if s_count[left_char] == 0:
#                 del s_count[left_char]

#             if s_count == p_count:
#                 output.append(i - p_len + 1)

#         return output