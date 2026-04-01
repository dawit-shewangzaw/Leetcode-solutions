class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # We hit a mismatch! 
                # We try two separate paths:
                
                # Path A: Skip the character at 'left'
                # Check if s[left+1 ... right] is a palindrome
                skip_left = s[left + 1 : right + 1]
                
                # Path B: Skip the character at 'right'
                # Check if s[left ... right-1] is a palindrome
                skip_right = s[left : right]
                
                # If either one is a palindrome, return True
                return (skip_left == skip_left[::-1]) or (skip_right == skip_right[::-1])
        
        return True
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         # check if a slice of s is a perfect palindrome
#         def is_perfect_palindrome(left, right):
#             while left < right:
#                 if s[left] != s[right]:
#                     return False
#                 left += 1
#                 right -= 1
#             return True

#         left, right = 0, len(s) - 1
        
#         while left < right:
#             if s[left] != s[right]:
#                 # We found a mismatch! We use our 'one chance' here.
#                 # Choice 1: Skip s[left] -> check s[left+1...right]
#                 # Choice 2: Skip s[right] -> check s[left...right-1]
#                 return is_perfect_palindrome(left + 1, right) or \
#                        is_perfect_palindrome(left, right - 1)
            
#             left += 1
#             right -= 1
            
#         return True


# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         left = 0
#         right = len(s) - 1
#         check = 0
        
#         while left <= right:
#             print("s[left] " + str(s[left]))
#             print("s[right] " + str(s[right]))
#             if s[left] == s[right]:
#                 left += 1
#                 right -= 1
#             else:
#                 if s[left] == s[right - 1]:
#                     right -= 1
#                 elif s[left + 1] == s[right]:
#                     left += 1

#                 if check >= 2:
#                     return False
#                 else:
#                     left += 1
#                     right -= 1
#                     check += 1
#         return True