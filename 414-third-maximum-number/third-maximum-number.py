class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = sorted(list(set(nums)) , reverse = True)
    
        if len(unique_nums) >= 3:
            output = unique_nums[2]
        else:
            output = unique_nums[0]
        return output