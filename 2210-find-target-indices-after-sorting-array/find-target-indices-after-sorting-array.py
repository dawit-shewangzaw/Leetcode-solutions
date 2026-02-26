class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        val = []
        tot_count = len(nums)
        for i in range(tot_count):
            if nums[i] == target:
                val += [i]
        return val