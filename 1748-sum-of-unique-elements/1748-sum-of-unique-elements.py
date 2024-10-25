class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(num for num, count in Counter(nums).items() if count == 1)
