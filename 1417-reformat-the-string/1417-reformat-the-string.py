class Solution:
    def reformat(self, s: str) -> str:
        # Separate letters and digits into two lists
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]

        # Check if reformatting is possible
        if abs(len(letters) - len(digits)) > 1:
            return ""  # Not possible to interleave

        # Make sure the longer list is first for interleaving
        if len(letters) < len(digits):
            letters, digits = digits, letters

        # Interleave letters and digits
        result = []
        for i in range(len(s)):
            if i % 2 == 0:
                result.append(letters.pop())
            else:
                result.append(digits.pop())

        return "".join(result)
