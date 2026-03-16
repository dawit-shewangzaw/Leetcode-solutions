class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(goal):
            if goal < 0: return 0
            left = 0
            count = 0
            ans = 0
            
            for right in range(len(nums)):
                
                if nums[right] % 2 != 0:
                    goal -= 1
                
                while goal < 0:
                    if nums[left] % 2 != 0:
                        goal += 1
                    left += 1
                
                ans += (right - left + 1)
            return ans

        return atMost(k) - atMost(k - 1)