class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        return -1
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         q = []
#         for i in s:
#             x = s.count(i)
#             if x == 1:
#                 y = s.index(i)
#                 q += [y]
#         if len(q) <= 0:
#             return -1
#         else:
#             return q[0]