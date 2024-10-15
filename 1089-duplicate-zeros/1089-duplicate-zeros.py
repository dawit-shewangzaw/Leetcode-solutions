class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                arr.insert(i+1, 0)  # Insert an extra 0 right after the current 0
                arr.pop()        # Remove the last element to maintain the original length
                i += 1           # Skip the next element (which is the duplicated 0)
            i += 1
