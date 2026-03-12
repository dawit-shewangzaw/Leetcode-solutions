class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr_length = len(nums)
        holder = 0 
        seeker = 0

        while seeker < arr_length:
            if nums[seeker] != 0:
                nums[seeker] , nums[holder] = nums[holder] , nums[seeker]
                holder += 1
            seeker += 1
        return nums