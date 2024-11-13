class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # Initialize the target array
        target = []
        
        # Insert each number at the specified index
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        
        return target
