class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left , right = 0 , int(sqrt(c))
        
        while left <= right:
            value = (left**2) + (right**2) 
            if value == c:
                return True
            elif value > c:
                right -= 1
            else:
                left += 1
        return False