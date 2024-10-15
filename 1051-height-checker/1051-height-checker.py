class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)  # Sort the heights to get the expected order
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count

        