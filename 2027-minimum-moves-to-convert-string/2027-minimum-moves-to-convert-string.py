class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = i = 0
        while i < len(s):
            if s[i] == 'X':
                moves += 1
                i += 3  # Skip next two characters as they are converted to 'O'
            else:
                i += 1
        return moves
