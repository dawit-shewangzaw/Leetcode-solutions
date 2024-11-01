class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]

            # Move forward until the end of the current range
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1

            # Format the range based on start and end values
            if start == nums[i]:
                result.append(str(start))  # Single element range
            else:
                result.append(f"{start}->{nums[i]}")  # Multiple element range

            i += 1

        return result
