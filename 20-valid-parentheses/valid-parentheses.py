class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict  = {'(': ')',  '{': '}', '[': ']' }
        
        for i in range(len(s)):
            if s[i] in my_dict.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                a = stack.pop()
                if s[i] != my_dict[a]:
                    return False
        return not stack
        
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
        
#         mapping = {
#             ')': '(',
#             '}': '{',
#             ']': '['
#         }
#         for char in s:
#             if char in mapping:
#                 if not stack or stack[-1] != mapping[char]:
#                     return False
#                 stack.pop()
#             else:
#                 stack.append(char)
        
#         return len(stack) == 0