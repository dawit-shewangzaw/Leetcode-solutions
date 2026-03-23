class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        nums_length = len(nums)
        res = [-1] * nums_length
        current_sum = 0
        window_size = 2 * k + 1
        
        if nums_length < window_size:
            return res
        
        for i in range(window_size):
            current_sum += nums[i]

        for i in range(k, nums_length - k):
            res[i] = current_sum // window_size
            
            if i + k + 1 < nums_length:
                current_sum += nums[i + k + 1]
                current_sum -= nums[i - k]
        return res