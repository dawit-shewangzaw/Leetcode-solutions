class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_sum = 0
        current_sum = 0
        window_set = set()
        left = 0
        
        for right in range(n):
            
            while nums[right] in window_set:
                window_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1
                
            window_set.add(nums[right])
            current_sum += nums[right]
            
            if right - left + 1 > k:
                window_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
                
        return max_sum

# class Solution:
#     def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # ans = 0
        # current_sum = 0
        # begin = 0
        # end = 0
        # num_to_index = {}

        # while end < len(nums):
        #     curr_num = nums[end]
        #     last_occurrence = num_to_index.get(curr_num, -1)
        #     # if current window already has number or if window is too big, adjust window
        #     while begin <= last_occurrence or end - begin + 1 > k:
        #         current_sum -= nums[begin]
        #         begin += 1
        #     num_to_index[curr_num] = end
        #     current_sum += nums[end]
        #     if end - begin + 1 == k:
        #         ans = max(ans, current_sum)
        #     end += 1
        # return ans