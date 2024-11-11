class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid  # Narrow down to the left part
            else:
                left = mid + 1  # Move to the right part
        return left
