class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        # Step 1: Find minimum and maximum values in nums
        min_val, max_val = min(nums), max(nums)
        
        # If all elements are the same, the max gap is 0
        if min_val == max_val:
            return 0
        
        # Step 2: Calculate bucket size and bucket count
        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # Step 3: Initialize buckets
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        
        # Step 4: Place each number in its corresponding bucket
        for num in nums:
            index = (num - min_val) // bucket_size
            buckets[index][0] = min(buckets[index][0], num)  # Update min in bucket
            buckets[index][1] = max(buckets[index][1], num)  # Update max in bucket

        # Step 5: Calculate the maximum gap
        max_gap = 0
        previous_max = min_val
        
        for bucket_min, bucket_max in buckets:
            # Only consider non-empty buckets
            if bucket_min == float('inf') and bucket_max == float('-inf'):
                continue
            max_gap = max(max_gap, bucket_min - previous_max)
            previous_max = bucket_max

        return max_gap
