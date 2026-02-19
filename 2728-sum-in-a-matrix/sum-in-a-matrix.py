class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:

        for row in nums:
            row.sort()

        score = 0
        rows = len(nums)
        cols = len(nums[0])

        for c in range(cols - 1, -1, -1):
            col_max = 0
            for r in range(rows):
                col_max = max(col_max, nums[r][c])
            score += col_max

        return score
