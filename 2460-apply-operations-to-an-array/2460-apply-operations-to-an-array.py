class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # First, apply the operations to modify the array
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Now, we need to shift all non-zero elements to the front
        result = []

        # Collect all non-zero elements
        for num in nums:
            if num != 0:
                result.append(num)

        # Fill the remaining with zeros
        result += [0] * (n - len(result))

        return result
