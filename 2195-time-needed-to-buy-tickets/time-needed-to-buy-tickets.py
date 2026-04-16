class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = 0
        target_tickets = tickets[k]
        
        for i in range(len(tickets)):
            if i <= k:
                total_time += min(tickets[i], target_tickets)
            else:
                total_time += min(tickets[i], target_tickets - 1)
                
        return total_time