class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Define binary search range
        left, right = 1, max(quantities)
        
        # Function to check if a given x is feasible
        def canDistribute(x):
            stores_needed = 0
            for quantity in quantities:
                stores_needed += math.ceil(quantity / x)
            return stores_needed <= n

        # Perform binary search
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid  # Try to find a smaller maximum load
            else:
                left = mid + 1  # Increase the load to make it feasible

        return left
