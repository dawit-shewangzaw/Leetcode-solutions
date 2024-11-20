from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Step 1: Count characters and validate
        count = Counter(s)
        if count['a'] < k or count['b'] < k or count['c'] < k:
            return -1
        
        # Step 2: Sliding window to find the largest removable substring
        n = len(s)
        target = {'a': count['a'] - k, 'b': count['b'] - k, 'c': count['c'] - k}
        current_count = {'a': 0, 'b': 0, 'c': 0}
        max_window = 0
        left = 0
        
        for right in range(n):
            current_count[s[right]] += 1
            while (current_count['a'] > target['a'] or
                   current_count['b'] > target['b'] or
                   current_count['c'] > target['c']):
                current_count[s[left]] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)
        
        # Step 3: Calculate the minimum time
        return n - max_window
