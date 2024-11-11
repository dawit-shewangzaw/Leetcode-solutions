class Solution:
    def isBalanced(self, num: str) -> bool:
        even = []
        odd = []
        even_sum = 0
        odd_sum = 0
        for i in range(len(num)):
            if i % 2 == 0:
                even.append(num[i])
            else:
                odd.append(num[i])
        for i in even:
            even_sum += int(i)
        for i in odd:
            odd_sum += int(i)
        if even_sum == odd_sum:
            return True
        else:
            return False