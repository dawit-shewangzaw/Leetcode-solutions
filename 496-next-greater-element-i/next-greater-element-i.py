class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_map = {}
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                smaller_num = stack.pop()
                greater_map[smaller_num] = num
            
            stack.append(num)
            
        return [greater_map.get(n, -1) for n in nums1]