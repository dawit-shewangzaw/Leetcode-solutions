class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        while n >= rows + 1:
            rows += 1
            n -= rows
        return rows
    
# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         # If there is 0 n values
#         if n == 0:
#             return 0
#         count = 0
#         for i in range(1,n+1):
#             n = n - i  
#             if n >= 0:
#                 count += 1
#         return count
    