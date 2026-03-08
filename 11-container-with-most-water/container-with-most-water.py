class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            
            width = right - left
            h = min(height[left], height[right])
            current_area = width * h
            
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

        # output = 1

        # for i in range(len(height) - 1):
        #     for j in range(1, len(height)):
        #         min_value = min(height[i] , height[j]) 
        #         max_value = (j - i) * min_value

        #         if max_value > output:
        #             output = max_value
                    
        # return output