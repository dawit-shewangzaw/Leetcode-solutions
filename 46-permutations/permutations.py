class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(current_path, used_mask):
            
            if len(current_path) == len(nums):
                res.append(current_path[:])
                return
            
            for i in range(len(nums)):
                if not used_mask[i]:
                    
                    used_mask[i] = True
                    current_path.append(nums[i])
                    
                    backtrack(current_path, used_mask)
                    
                    current_path.pop()
                    used_mask[i] = False
        
        backtrack([], [False] * len(nums))
        return res