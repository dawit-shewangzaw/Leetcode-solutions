class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        student = 0
        for index , i in enumerate(endTime):
            if i >= queryTime:
                if startTime[index] <= queryTime:
                    student += 1
        return student