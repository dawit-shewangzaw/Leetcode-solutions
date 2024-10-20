class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # Split the date into year, month, and day
        year, month, day = date.split("-")

        # Convert year, month, and day to integers
        year = int(year)
        month = int(month)
        day = int(day)

        # Convert each part to binary and remove the '0b' prefix
        year_bin = bin(year)[2:]
        month_bin = bin(month)[2:]
        day_bin = bin(day)[2:]

        # Return the concatenated result in 'year-month-day' format
        return f"{year_bin}-{month_bin}-{day_bin}"

        