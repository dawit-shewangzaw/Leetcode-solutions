import math

class Solution:
    def constructRectangle(self, area: int) -> list:
        # Start from the integer square root of the area
        width = int(math.sqrt(area))
        
        # Find the pair (L, W) such that L * W = area
        while area % width != 0:
            width -= 1
        
        length = area // width
        return [length, width]
