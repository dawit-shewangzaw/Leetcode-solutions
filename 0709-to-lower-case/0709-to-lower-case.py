class Solution:
    def toLowerCase(self, s: str) -> str:
        output = ""
        for i in range (len(s)):
            x = s[i]
            if x.islower():
                output += x
            else:
                y = x.lower()
                output += y
        return output