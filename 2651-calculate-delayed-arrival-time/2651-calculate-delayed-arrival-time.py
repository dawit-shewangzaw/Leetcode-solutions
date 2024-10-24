class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        train_arr = arrivalTime + delayedTime
        if train_arr == 24:
            train_arr = 0
        elif train_arr > 24:
            train_arr = train_arr - 24
        return train_arr
        