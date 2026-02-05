class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        count_map = {}

        # Store first index of each number in sorted array
        for i, num in enumerate(sorted_nums):
            if num not in count_map:
                count_map[num] = i

        # Build result
        return [count_map[num] for num in nums]
