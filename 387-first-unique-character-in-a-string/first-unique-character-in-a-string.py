class Solution:
    def firstUniqChar(self, s: str) -> int:
        x = Counter(s)
        
        for i in range(len(s)):
            value = x[s[i]]
            if value == 1:
                return i
        return -1
        
        