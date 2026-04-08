class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr_len = len(arr)
        left , right = 0 , 1

        if 1 not in arr:
            arr[0] = 1
        
        while right < arr_len:
            if arr[left] == arr[right] or arr[left] + 1 == arr[right]:
                left += 1
                right += 1
            else:
                arr[right] = arr[left] + 1  
        print(arr)
        return max(arr)