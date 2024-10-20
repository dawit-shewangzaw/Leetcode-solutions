class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        cycle_length = 2 * (n - 1)  # Total length of a right and left pass
        remaining_moves = k % cycle_length  # Find how far we are into the cycle

        if remaining_moves < n:
            return remaining_moves  # Moving right, so return the index
        else:
            # Moving left, calculate how far back from the right end
            return 2 * (n - 1) - remaining_moves