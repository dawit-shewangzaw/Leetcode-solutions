class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        # Calculate LIS from the left to right
        lis_left = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis_left[i] = max(lis_left[i], lis_left[j] + 1)
        
        # Calculate LIS from the right to left
        lis_right = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    lis_right[i] = max(lis_right[i], lis_right[j] + 1)
        
        # Calculate the maximum mountain length
        max_mountain_len = 0
        for i in range(1, n - 1):
            if lis_left[i] > 1 and lis_right[i] > 1:
                max_mountain_len = max(max_mountain_len, lis_left[i] + lis_right[i] - 1)
        
        # Minimum removals to make it a mountain array
        return n - max_mountain_len
