from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        # Count the frequency of each character
        count = Counter(s)
        result = []

        # Get the sorted list of unique characters
        chars = sorted(count.keys())

        while len(result) < len(s):
            # Step 1: Pick the smallest characters in lexicographical order
            for char in chars:
                if count[char] > 0:
                    result.append(char)
                    count[char] -= 1

            # Step 2: Pick the largest characters in reverse lexicographical order
            for char in reversed(chars):
                if count[char] > 0:
                    result.append(char)
                    count[char] -= 1

        return ''.join(result)
