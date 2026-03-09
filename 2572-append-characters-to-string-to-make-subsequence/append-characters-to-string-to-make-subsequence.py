class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        n, m = len(s), len(t)
        j = 0
        
        for i in range(n):
            if s[i] == t[j]:
                j += 1
                
                if j == m:
                    return 0
        
        return m - j