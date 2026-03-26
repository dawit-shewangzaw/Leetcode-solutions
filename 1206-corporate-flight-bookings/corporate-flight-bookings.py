class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 2)
        
        for first, last, seats in bookings:
            diff[first] += seats
        
            if last + 1 <= n:
                diff[last + 1] -= seats
        
        result = [0] * n
        current_seats = 0
        for i in range(1, n + 1):
            current_seats += diff[i]
            result[i - 1] = current_seats
            
        return result

# class Solution:
#     def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
#         output = [0] * (n + 1)
#         value = 1
#         while value <= n:
#             for i in range(len(bookings)):
#                 if (value == bookings[i][0]) or ((value >= bookings[i][0]) and (value <= bookings[i][1])):
#                     output[value] += bookings[i][2]
#             value += 1
#         output = output[1:] 
#         return output