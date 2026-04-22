class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        nums_len = len(nums)
        low, high = 0, nums_len

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low += 1
        return -1