from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Dictionary to store the sum of digits as keys and their frequencies as values
        groups = defaultdict(int)

        # Calculate the sum of digits for each number from 1 to n and count in groups
        for num in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(num))
            groups[digit_sum] += 1

        # Find the maximum size of any group
        max_size = max(groups.values())

        # Count how many groups have this maximum size
        largest_groups_count = sum(1 for size in groups.values() if size == max_size)

        return largest_groups_count
