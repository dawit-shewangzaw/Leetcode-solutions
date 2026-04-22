class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(t):
            low, high = 0, len(nums)
            
            while low < high:
                mid = (low + high) // 2
                
                if nums[mid] < t:
                    low = mid + 1
                else:
                    high = mid
            return low
        fo = search(target)
        lo = search(target + 1) - 1

        if fo < len(nums) and nums[fo] == target:
            return [fo , lo]
        
        return [-1,-1]