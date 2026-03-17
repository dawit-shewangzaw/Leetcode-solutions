class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        limit = n // 4
        counts = Counter(s)
        
        # If nothing is over the limit, we need 0 replacements
        if all(counts[c] <= limit for c in "QWER"):
            return 0
            
        ans = n
        left = 0
        
        for right in range(n):
            # Move 'right' to put a character INTO the replacement box
            counts[s[right]] -= 1
            
            # While the characters OUTSIDE the box are all safe (<= limit)
            while left < n and all(counts[c] <= limit for c in "QWER"):
                # Update our minimum window size
                ans = min(ans, right - left + 1)
                
                # Try to shrink the box from the left
                counts[s[left]] += 1
                left += 1
                
        return ans