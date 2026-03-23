class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        res = [1] * nums_length
        
        left = 1
        for i in range(nums_length):
            res[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(nums_length - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         nums_length = len(nums)
#         output = []
#         prefix_mul = 1
        
#         for i in range(nums_length):
#             prefix_mul *= nums[i]
#         for i in range(nums_length):
#             value = int(prefix_mul / nums[i])
#             output += [value]
#         return output