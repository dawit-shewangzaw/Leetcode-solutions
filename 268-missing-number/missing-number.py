class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums) + 1):
            if i == len(nums) or nums[i] != i:
                return i
# class Solution:
#     def missingNumber(self, nums: list[int]) -> int:
#         n = len(nums)
#         total = n * (n + 1) // 2
#         return total - sum(nums)