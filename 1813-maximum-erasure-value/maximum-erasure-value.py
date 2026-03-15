class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        unique = set()
        max_score = float("-inf")
        arr_sum = 0
        left = 0

        for right in range(len(nums)):

            while nums[right] in unique:
                unique.remove(nums[left])
                arr_sum -= nums[left]
                left += 1
            
            unique.add(nums[right])
            arr_sum += nums[right]
            max_score = max(max_score , arr_sum)
        return max_score