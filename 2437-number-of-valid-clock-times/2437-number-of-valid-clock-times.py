class Solution:
    def countTime(self, time: str) -> int:
        # Determine the number of choices for hours
        if time[0] == '?' and time[1] == '?':
            hour_combinations = 24  # Covers all hours from "00" to "23"
        elif time[0] == '?':
            # If time[0] is ?, consider the constraints of time[1]
            hour_combinations = 3 if int(time[1]) <= 3 else 2
        elif time[1] == '?':
            # If time[1] is ?, consider the constraints of time[0]
            hour_combinations = 10 if time[0] in '01' else 4
        else:
            # No ? in the hour part, just 1 possibility for this specific time
            hour_combinations = 1

        # Determine the number of choices for minutes
        minute_combinations = (6 if time[3] == '?' else 1) * (10 if time[4] == '?' else 1)

        # Total combinations
        return hour_combinations * minute_combinations
