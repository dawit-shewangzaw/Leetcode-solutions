class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Counter to track consecutive odd numbers
        count = 0
        
        for num in arr:
            # Check if the current number is odd
            if num % 2 != 0:
                count += 1
                # Check if we have found three consecutive odds
                if count == 3:
                    return True
            else:
                # Reset counter if the current number is not odd
                count = 0
                
        # Return False if we never found three consecutive odd numbers
        return False
