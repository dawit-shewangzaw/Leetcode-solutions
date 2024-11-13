from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Count frequencies of each number
        freq = Counter(arr)
        
        # Initialize variable to store the largest lucky integer
        largest_lucky = -1
        
        # Check each number and its frequency
        for num, count in freq.items():
            # If the number is "lucky" (its frequency equals its value)
            if num == count:
                # Update the largest lucky integer if necessary
                largest_lucky = max(largest_lucky, num)
                
        return largest_lucky
