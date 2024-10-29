class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(row: int, col: int) -> int:
            if col == n - 1:
                return 0
            if dp[row][col] != -1:
                return dp[row][col]
            
            max_moves = 0
            directions = [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]
            for r, c in directions:
                if 0 <= r < m and 0 <= c < n and grid[r][c] > grid[row][col]:
                    max_moves = max(max_moves, 1 + dfs(r, c))
            
            dp[row][col] = max_moves
            return max_moves
        
        max_result = 0
        for row in range(m):
            max_result = max(max_result, dfs(row, 0))
        
        return max_result
