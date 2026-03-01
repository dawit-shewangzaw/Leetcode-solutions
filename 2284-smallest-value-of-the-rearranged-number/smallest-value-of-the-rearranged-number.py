class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        negative = num < 0
        num = abs(num)

        count = [0] * 10
        while num > 0:
            count[num % 10] += 1
            num //= 10

        result = []

        if not negative:
            for i in range(1, 10):
                if count[i] > 0:
                    result.append(str(i))
                    count[i] -= 1
                    break

            result.extend(['0'] * count[0])

            for i in range(1, 10):
                result.extend([str(i)] * count[i])

            return int("".join(result))

        else:
            for i in range(9, -1, -1):
                result.extend([str(i)] * count[i])

            return -int("".join(result))