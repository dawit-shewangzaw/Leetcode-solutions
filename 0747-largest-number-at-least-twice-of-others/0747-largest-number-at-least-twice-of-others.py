class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0  # If there's only one number, return index 0

        # Sort the array and find the two largest numbers
        x = sorted(nums)
        y = x[-1]  # Largest number
        z = x[-2] * 2  # Twice the second largest number
        
        if y >= z:
            return nums.index(y)  # Return the index of the largest number
        else:
            return -1  # if the largest number is not at least twice as large as the second largest
