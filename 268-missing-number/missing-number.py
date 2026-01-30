# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums) + 1
#         i = 0
#         for i in range (n):
#             if i in nums:
#                 i = i + 1
#             else: 
#                 return i
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)
