class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dp(i, j):
            if i == m-1 and j == n-1:
                return {grid[i][j]}
            hset = set()
            if i + 1 < m:
                for val in dp(i+1, j):
                    hset.add(grid[i][j] ^ val)
            if j + 1 < n:
                for val in dp(i, j+1):
                    hset.add(grid[i][j] ^ val)
            return hset
        return min(dp(0, 0))