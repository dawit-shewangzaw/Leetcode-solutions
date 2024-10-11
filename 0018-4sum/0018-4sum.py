class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # Sort the array to make it easier to handle duplicates and use two-pointer technique
        nums.sort()
        result = []
        n = len(nums)
        
        # First two loops to select the first two numbers
        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Two pointers for the rest of the array
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        # Skip duplicates for the third number
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # Skip duplicates for the fourth number
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                        
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return result
