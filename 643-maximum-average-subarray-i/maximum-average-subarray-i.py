class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # First we make the window result
        total = sum(nums[0:k]) 
        output = total 

        for i in range(len(nums)-k):
            # Add the right next num to total
            total += nums[i+k]
            # Substruct the most left nums from the window 
            total -= nums[i]
            # Compare from the past total and assign the maximum to the output  
            output = max(total ,output)
        return output/k