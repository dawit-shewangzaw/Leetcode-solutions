class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = len(nums)
        output = 0
        for i in range(count - 1):
            for j in range(1 , count):
                value = nums[i] + nums[j]
                if i < j and value < target:
                    output += 1
        
        return output
        
# class Solution:
#     def countPairs(self, nums: List[int], target: int) -> int:
#         nums.sort()
        
#         left = 0
#         right = len(nums) - 1
#         output = 0
        
#         while left < right:
#             if nums[left] + nums[right] < target:
#                 output += (right - left)
#                 left += 1
#             else:
#                 right -= 1
                
#         return output
