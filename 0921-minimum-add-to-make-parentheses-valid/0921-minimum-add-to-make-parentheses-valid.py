class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_pras = 0
        min_adds_req = 0
        for letter in s :
            if letter == "(":
                open_pras += 1
            else:
                if open_pras > 0 :
                    open_pras -= 1
                else:
                    min_adds_req += 1
        return min_adds_req + open_pras