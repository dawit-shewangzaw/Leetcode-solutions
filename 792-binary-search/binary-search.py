# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
        
#         nums_len = len(nums)
#         low, high = 0, nums_len

#         while low < high:
#             mid = low + (high - low) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 high = mid
#             else:
#                 low += 1
#         return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        nums_len = len(nums)
        low, high = 0, nums_len - 1

        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1