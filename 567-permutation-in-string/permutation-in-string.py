class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_counter = Counter(s1)
        x = len(s1)
        left = 0
        right = x

        while right <= len(s2):

            substring = s2[left : right]
            sub_counter = Counter(substring)
            if sub_counter == s1_counter:
                return True
            else:
                left += 1
                right += 1
        return False