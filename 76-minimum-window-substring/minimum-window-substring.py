# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         hash_s = {}
#         hash_t = {}
#         #building our t
#         for char in t:
#             hash_t[char] = 1 + hash_t.get(char , 0)
#         need = len(t)
#         count = 0
#         l = 0
#         r_index = 0
#         l_index = 0
#         ans = float("inf")
#         for r in range(len(s)):
#             hash_s[s[r]] = 1 + hash_s.get(s[r] , 0)
#             if s[r] in hash_t and hash_t[s[r]] == hash_s[s[r]]:
#                 count += 1
#             #shrinking our window
#             while count == need:
#                 if (r - l + 1) < ans:
#                     ans = r - l + 1
#                     l_index = l
#                     r_index = r

#                 hash_s[s[l]] -= 1
#                 if s[l] in hash_t and hash_s[s[l]] < hash_t[s[l]]:
#                     count -= 1
#                 l += 1
#         return s[l_index:r_index + 1] if ans != float("inf") else ""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)
        l, r = 0, 0
        formed = 0
        window_counts = {}

        ans = float("inf"), None, None

        while r < len(s):
            
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            while l <= r and formed == required:
                char = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                l += 1    

            r += 1    
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]