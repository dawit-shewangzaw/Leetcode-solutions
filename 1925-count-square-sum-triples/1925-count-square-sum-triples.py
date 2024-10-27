class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = (a * a + b * b) ** 0.5
                if c.is_integer() and c <= n:
                    count += 1
        return count
