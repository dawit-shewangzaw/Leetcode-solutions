class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        # Calculate the number of turns that can be played
        turns = min(x, y // 4)
        
        # If the number of turns is odd, Alice wins (she plays the last turn)
        if turns % 2 == 1:
            return "Alice"
        # If the number of turns is even, Bob wins (he plays the last turn)
        else:
            return "Bob"
