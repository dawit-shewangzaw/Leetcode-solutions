class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = [] 

        for i in range(2 * n):
            current_num = nums[i % n]
            
            while stack and nums[stack[-1]] < current_num:
                index = stack.pop()
                res[index] = current_num
            
            if i < n:
                stack.append(i)
                
        return res