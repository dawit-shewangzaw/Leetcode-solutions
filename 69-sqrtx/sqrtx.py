class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            mid_sq = mid * mid

            if mid_sq == x:
                return mid
            elif mid_sq > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1

        return ans

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         i = 0
#         while(True):
#             if (i * i == x):
#                 return i
#             elif ( i * i > x):
#                 return i - 1
#             else:
#                 i += 1