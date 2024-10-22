class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        under = []
        above = []
        for i in nums:
            if i < 10:
                under += [i]
            elif i >= 10:
                above += [i]
        sum_under = 0
        sum_above = 0
        for i in under:
            sum_under += i
        for i in above:
            sum_above += i
            
        result = True
        if sum_under == sum_above :
            result = False
        else:
            result = True
        return result
        