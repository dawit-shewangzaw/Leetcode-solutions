class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        left, right = 0, nums_len

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left += 1
        return -1