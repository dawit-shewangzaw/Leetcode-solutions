class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def backtrack(index: int, current_sum: int) -> int:
            if index == len(nums):
                return 1 if current_sum == target else 0

            # Explore both adding and subtracting the current number
            add = backtrack(index + 1, current_sum + nums[index])
            subtract = backtrack(index + 1, current_sum - nums[index])

            return add + subtract

        return backtrack(0, 0)
