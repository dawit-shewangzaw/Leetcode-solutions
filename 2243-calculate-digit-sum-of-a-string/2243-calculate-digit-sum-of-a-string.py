class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ""
            # Divide into groups of size k
            for i in range(0, len(s), k):
                group = s[i:i + k]
                # Calculate the sum of the digits in the group
                group_sum = sum(int(c) for c in group)
                new_s += str(group_sum)
            # Replace s with the new concatenated string
            s = new_s
        return s
        