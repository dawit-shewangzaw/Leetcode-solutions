class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []

        for x in nums:
            index = abs(x) - 1

            if nums[index] < 0:
                duplicates.append(abs(x))
            else:
                nums[index] = -nums[index]

        return duplicates
