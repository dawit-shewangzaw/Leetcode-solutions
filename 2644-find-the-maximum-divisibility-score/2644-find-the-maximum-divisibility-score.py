class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_score = -1
        result_divisor = float('inf')

        for divisor in divisors:
            score = sum(1 for num in nums if num % divisor == 0)

            if score > max_score or (score == max_score and divisor < result_divisor):
                max_score = score
                result_divisor = divisor

        return result_divisor