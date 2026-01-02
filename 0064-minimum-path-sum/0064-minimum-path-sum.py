class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @lru_cache(None)
        def dp(i, j):
            if i < 0 or j < 0:
                return float('inf')
            if i == 0 and j == 0:
                return grid[i][j]
            return grid[i][j] + min(dp(i-1, j), dp(i, j - 1))
        return dp(m-1, n-1)