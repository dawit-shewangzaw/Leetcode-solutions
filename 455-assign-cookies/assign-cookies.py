class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        output = 0
        left , right = 0 , 0

        while left<len(s) and right<len(g):
            if(s[left] >= g[right]):
                output += 1
                left += 1
                right += 1
            else:
                left += 1
        return output