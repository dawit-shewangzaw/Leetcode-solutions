import heapq
import math

class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        # Max-heap implementation using negative values
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        
        # Perform k operations
        for _ in range(k):
            # Get the largest element (negate to get the original value)
            largest = -heapq.heappop(max_heap)
            score += largest
            
            # Replace the element with ceil(largest / 3)
            new_value = math.ceil(largest / 3)
            heapq.heappush(max_heap, -new_value)
        
        return score
