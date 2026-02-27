class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        total_arr2 = len(arr2)
        total_arr1 = len(arr1)
        In_both = []
        unique = []
        arr1.sort()

        # Get all that is not in arr2
        for i in range(total_arr1):
            if arr1[i] not in  arr2:
                unique += [arr1[i]]
        # Get all arr1 with arr2 setup
        for i in range(total_arr2):
            for j in range(total_arr1):
                if arr2[i] == arr1[j]:
                    In_both += [arr1[j]]
        # Append unique values at the end
        for i in range(len(unique)):
            In_both.append(unique[i])  
            
        return In_both