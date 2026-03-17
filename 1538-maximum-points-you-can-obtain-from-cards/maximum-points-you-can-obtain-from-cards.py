class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k
        
        total_sum = sum(cardPoints)
        
        if k == n:
            return total_sum
        
        current_window_sum = 0
        for i in range(window_size):
            current_window_sum += cardPoints[i]
            
        min_window_sum = current_window_sum
        
        left = 0
        for right in range(window_size, n):
            current_window_sum += cardPoints[right]
            current_window_sum -= cardPoints[left]
            left += 1
            
            min_window_sum = min(min_window_sum, current_window_sum)
            
        return total_sum - min_window_sum


# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:

#         arr_sum = 0
#         max_no = float("-inf")
#         left , right = 0 , k
#         turn = 0
        
#         for _ in range(k):
#             arr_sum += cardPoints[_]
#             print("arr_sum " + str(arr_sum))

#         max_no = max(max_no , arr_sum)
#         print("max_no " + str(max_no))
        
#         while right < len(cardPoints):

#             arr_sum += cardPoints[right]
#             arr_sum -= cardPoints[left]

#             right += 1
#             left += 1
#             max_no = max(max_no , arr_sum)
#             print("max_no " + str(max_no))
#         max_no = max(max_no , arr_sum)
#         print("final " + str(max_no))
        
#         return max_no