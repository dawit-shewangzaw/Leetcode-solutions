class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_unique = sorted(set(nums))
        
        res = n
        right = 0
        
        for left in range(len(sorted_unique)):
            
            max_allowed = sorted_unique[left] + n - 1
            
            while right < len(sorted_unique) and sorted_unique[right] <= max_allowed:
                right += 1
        
            keepers = right - left
            res = min(res, n - keepers)
            
        return res