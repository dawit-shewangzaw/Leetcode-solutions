class Solution:
    def maximumDifference(self, nums):
        min_value = nums[0]  # Initialize with the first element
        max_diff = -1  # Start with -1 in case no valid i, j is found
        
        # Traverse the array starting from the second element
        for j in range(1, len(nums)):
            if nums[j] > min_value:
                # Calculate difference if nums[j] is greater than the current minimum
                max_diff = max(max_diff, nums[j] - min_value)
            else:
                # Update min_value to the smaller value if found
                min_value = nums[j]
                
        return max_diff
