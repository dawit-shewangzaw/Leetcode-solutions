class Solution:
    def minimumSteps(self, s: str) -> int:
        steps = 0
        count_black = 0

        for char in s:
            if char == '1':
                count_black += 1
            elif count_black > 0:
                steps += count_black

        return steps

        