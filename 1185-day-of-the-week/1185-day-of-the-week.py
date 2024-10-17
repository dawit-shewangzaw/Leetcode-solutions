import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Create a datetime object for the given date
        date = datetime.date(year, month, day)
        
        # List of days corresponding to the weekday index
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        # Get the weekday index (0 = Monday, 6 = Sunday)
        return days_of_week[date.weekday()]
