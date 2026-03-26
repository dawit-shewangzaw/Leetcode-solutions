class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        k = k % nums_length
        
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # Reverse the whole thing
        reverse(0, nums_length - 1)
        
        # Reverse the first k elements
        reverse(0, k - 1)
        
        # Reverse the remaining elements
        reverse(k, nums_length - 1)