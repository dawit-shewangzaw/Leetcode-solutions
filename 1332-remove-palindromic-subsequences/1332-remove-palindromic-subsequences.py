class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # If the string is empty, no steps are needed
        if not s:
            return 0
        # Check if the string is a palindrome
        if s == s[::-1]:
            return 1
        # If the string is not a palindrome, it can be removed in 2 steps
        return 2
