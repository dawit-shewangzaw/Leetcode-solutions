class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check_shipment(ship_weight):
            
            total_days = 1
            current_load = 0
            for weight in weights:
                if current_load + weight > ship_weight:
                    total_days += 1
                    current_load = 0
                current_load += weight

            return total_days <= days

        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            if check_shipment(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left