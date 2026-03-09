class Solution:
    def isPalindrome(self, s: str) -> bool:

        palindrome = ''
        s = s.lower()
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isnumeric():
                palindrome += s[i]
        
        reverse_palindrome = palindrome[::-1]
        if palindrome == reverse_palindrome:
            return True
        else:
            return False