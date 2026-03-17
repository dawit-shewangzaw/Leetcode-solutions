class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = 0
        output = []
        for i in range(len(nums)):
            sums += nums[i]
            output += [sums]
        return output
        