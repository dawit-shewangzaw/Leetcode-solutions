class Solution:
     def twoSum(self, numbers: List[int], target: int) -> List[int]:

        arr_length = len(numbers)
        left = 0
        right = arr_length - 1
        output = []

        while left < right:
            current_value = numbers[left] + numbers[right] 
            if current_value == target:
                output = [left + 1 , right + 1]
                return output
            elif current_value > target:
                right -= 1
            else:
                left += 1

        
#             left = 0 
#             right = len(numbers) - 1
#             sum = 0
#             while left <= right :
#                 sum = numbers[left] + numbers[right]
#                 if sum == target:
#                     return [left +1 , right + 1 ]
#                 elif sum <= target:
#                     left += 1
#                 else:
#                     right -= 1

# # class Solution:
# #     def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
# #         for i in range(len(numbers)):
# #             for j in range(len(numbers)):
# #                 if (i != j) and (numbers[i] + numbers[j] == target):
# #                     return [i + 1, j + 1]
        