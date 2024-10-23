class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Initialize a variable to track the maximum wealth
        max_wealth = 0
        
        # Loop through each customer's accounts
        for customer in accounts:
            # Calculate the wealth of the current customer
            wealth = sum(customer)
            # Update the max_wealth if the current wealth is greater
            max_wealth = max(max_wealth, wealth)
        
        # Return the maximum wealth found
        return max_wealth
