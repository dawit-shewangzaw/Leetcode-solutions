class Solution:
    def clearDigits(self, s: str) -> str:
    # Keep running the loop until no digits are left
        while any(c.isdigit() for c in s):
            for i in range(len(s)):
                if s[i].isdigit():
                    # Find the closest non-digit character to the left
                    for j in range(i - 1, -1, -1):
                        if not s[j].isdigit():
                            # Remove both the digit and the closest non-digit character
                            s = s[:j] + s[j+1:i] + s[i+1:]
                            break
                    break
        return s