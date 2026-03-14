class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        window_sum = float('-inf')
        left , right = 0 , k
        first_sum = 0

        for i in range(k):
            first_sum += nums[i]
            
        window_sum = max(first_sum , window_sum)

        while right < len(nums):
            first_sum += nums[right]
            first_sum -= nums[left]
        
            window_sum = max(window_sum , first_sum)
            left += 1
            right += 1
        
        return window_sum / k


        # for i in range(k):
        #     first_sum += nums[i]
            
        #     window_sum = max(first_sum , window_sum)
        
        # for right in range(k , len(nums)):
        #     first_sum += nums[right]
        #     first_sum -= nums[left]
        
        #     window_sum = max(window_sum , first_sum)
        #     left += 1
        
        # return window_sum / k
        
        # window_sum = float('-inf')
        # left = 0
        # first_sum = 0

        # for i in range(k):
        #     first_sum += nums[i]
            
        #     window_sum = max(first_sum , window_sum)
        
        # for right in range(k , len(nums)):
        #     first_sum += nums[right]
        #     first_sum -= nums[left]
        
        #     window_sum = max(window_sum , first_sum)
        #     left += 1
        
        # return window_sum / k










# # class Solution:
# #     def findMaxAverage(self, nums: List[int], k: int) -> float:
# #         # First we make the window result
# #         window_sum = sum(nums[0:k]) 
# #         output = window_sum 

# #         for i in range(len(nums)-k):
# #             # Add the right next num to window_sum
# #             window_sum += nums[i+k]
# #             # Substruct the most left nums from the window 
# #             window_sum -= nums[i]
# #             # Compare from the past window_sum and assign the maximum to the output  
# #             output = max(window_sum ,output)
# #         return output/k

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
        
#         window_sum = sum(nums[:k])
#         max_sum = window_sum
#         left = 0

#         for right in range(k,len(nums)):
#             window_sum += nums[right]
#             window_sum -= nums[left]
#             left += 1

#             max_sum = max(max_sum, window_sum)

#         return max_sum / k