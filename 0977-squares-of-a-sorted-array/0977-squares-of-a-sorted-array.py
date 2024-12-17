class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr = []
        for i in nums:
            i *= i
            sqr += [i]
        sqr.sort()
        
        return sqr
	
        