class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        
        for target in range(n, 1, -1):
            idx = arr.index(target)
            
            if idx == target - 1:
                continue
            
            if idx != 0:
                res.append(idx + 1)
                arr[:idx+1] = arr[:idx+1][::-1]
            
            res.append(target)
            arr[:target] = arr[:target][::-1]
            
        return res