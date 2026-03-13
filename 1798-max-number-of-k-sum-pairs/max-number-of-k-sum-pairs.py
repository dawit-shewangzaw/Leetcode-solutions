class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = len(nums)
        output = 0
        left = 0
        right = count - 1

        while left < right and len(nums) >= 2:
            value = nums[left] + nums[right]
            if value == k:
                output += 1
                left += 1
                right -= 1
            elif value < k :
                left += 1
            else:
                right -= 1

        return output