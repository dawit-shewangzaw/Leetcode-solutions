class NumArray:
    def __init__(self, nums: List[int]):
        
        self.nums = nums
        for i in range(1 , len(nums)):
            self.nums[i] += self.nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:

        if left == 0:
            return self.nums[right]
        else:
            return self.nums[right] - self.nums[left - 1]
       
# class NumArray:
#     def __init__(self, nums: List[int]):
        
#         self.prefix_sum = [0] * (len(nums) + 1)
#         for i in range(len(nums)):
#             self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

#     def sumRange(self, left: int, right: int) -> int:
        
#         return self.prefix_sum[right + 1] - self.prefix_sum[left]
       
       
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)