class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # Initialize the list with zeros, representing the number of candies each person gets
        distribution = [0] * num_people
        i = 0  # Starting index for distributing candies
        give = 1  # The amount of candy to give on each round
        
        # Continue the process until we run out of candies
        while candies > 0:
            distribution[i % num_people] += min(give, candies)  # Give the lesser of the remaining candies or the amount to give
            candies -= give  # Decrease the number of remaining candies
            give += 1  # Increase the amount of candy to give on the next round
            i += 1  # Move to the next person
        
        return distribution
