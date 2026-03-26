class Solution:
    def maxArea(self, height: List[int]) -> int:

        left , right = 0 , len(height) - 1
        max_height = float("-inf")

        while left < right:
            min_height = min(height[right] , height[left])
            i = (right - left) * min_height
            max_height = max(max_height , i)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
             
        return max_height 










        # left = 0
        # right = len(height) - 1
        # max_area = 0

        # while left < right:
            
        #     width = right - left
        #     h = min(height[left], height[right])
        #     current_area = width * h
            
        #     max_area = max(max_area, current_area)

        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1
                
        # return max_area