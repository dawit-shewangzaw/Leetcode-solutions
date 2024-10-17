class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Sort the array
        arr.sort()
        
        # Initialize the minimum difference to a large number
        min_diff = float('inf')
        result = []
        
        # Find the minimum absolute difference
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i - 1], arr[i]]]  # Start new result list
            elif diff == min_diff:
                result.append([arr[i - 1], arr[i]])  # Add the pair to the result list
        
        return result
