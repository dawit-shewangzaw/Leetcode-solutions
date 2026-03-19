class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}
        current_sum = 0
        
        for i in range(len(nums)):
            current_sum += nums[i]
            remainder = current_sum % k
            
            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i
                
        return False



# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         n = len(nums)
#         cumlative_sum = [0] * (n + 1)

#         for i in range(1 , n + 1):
#              cumlative_sum[i] = cumlative_sum[i - 1] + nums[i - 1]

#         for start in range(n):
#             for  end in range(start + 1, n):
#                 subarray_sum = cumlative_sum[end + 1] - cumlative_sum[start]
#                 if subarray_sum == 0 and k == 0:
#                     return True
#                 if k != 0 and subarray_sum % k == 0:
#                     return True
#         return False