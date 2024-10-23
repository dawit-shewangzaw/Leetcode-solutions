class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        greatest = -1  # Initialize the greatest element on the right as -1 (for the last element)

        # Traverse the array from right to left
        for i in range(n-1, -1, -1):
            # Temporarily store the current element
            current = arr[i]
            # Replace the current element with the greatest element to its right
            arr[i] = greatest
            # Update the greatest element
            greatest = max(greatest, current)
    
        return arr