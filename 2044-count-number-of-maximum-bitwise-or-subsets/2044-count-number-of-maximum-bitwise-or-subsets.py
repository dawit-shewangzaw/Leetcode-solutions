class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Step 1: Find the maximum possible bitwise OR of all elements
        max_or = 0
        for num in nums:
            max_or |= num
        
        # Step 2: Count the number of subsets that achieve this maximum OR
        def count_subsets(index, current_or):
            if index == len(nums):
                # If the current subset's OR equals the max OR, count it
                return 1 if current_or == max_or else 0
            # Two choices: include or exclude the current number in the subset
            include = count_subsets(index + 1, current_or | nums[index])
            exclude = count_subsets(index + 1, current_or)
            return include + exclude
        
        # Start from index 0 and an empty OR (0)
        return count_subsets(0, 0)
