class Solution:
    def binaryGap(self, n: int) -> int:        
        b = bin(n)[2:]
        
        last = -1
        max_dist = 0
        
        for i in range(len(b)):
            if b[i] == '1':
                if last != -1:
                    max_dist = max(max_dist, i - last)
                last = i
        
        return max_dist