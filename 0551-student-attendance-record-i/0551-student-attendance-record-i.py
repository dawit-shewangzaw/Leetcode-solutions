class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        los = "LLL"
        eli = ""
        for i in s:
            if i == "A":
                absent += 1
        if "LLL" in s :
            eli = False
        elif absent >= 2:
            eli = False
        else:
            eli = True
        return eli
        