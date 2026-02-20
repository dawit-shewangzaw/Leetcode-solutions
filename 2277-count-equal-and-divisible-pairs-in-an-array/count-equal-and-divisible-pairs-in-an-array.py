class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        tot = len(nums)
        for i in range(tot):
            for j in range(i + 1, tot):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    ans += 1
        return ans