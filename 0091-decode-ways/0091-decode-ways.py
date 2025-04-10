class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: empty string
        if not s:
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # There's one way to decode an empty string
        
        # If the first character is valid
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, n + 1):
            # Single digit decoding
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # Two-digit decoding
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]
