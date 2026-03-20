class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = nums[0]
        output = [sums]
        for i in range( 1 , len(nums)):
            sums += nums[i]
            output += [sums]
        return output
        
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         sums = 0
#         output = []
#         for i in range(len(nums)):
#             sums += nums[i]
#             output += [sums]
#         return output
        