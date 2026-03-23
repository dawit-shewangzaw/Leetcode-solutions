class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_length = len(nums)
        left_sum = 0
        total = sum(nums)

        for i in range(nums_length):

            right_sum = total - left_sum - nums[i]
            if right_sum == left_sum:
                return i
            left_sum += nums[i]

        return -1