class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = -1

        for num in nums:
            length = 0
            while num in nums_set:
                length += 1
                num *= num

            if length >= 2:
                max_length = max(max_length, length)

        return max_length
