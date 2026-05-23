class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0:
                return
            
            grid[r][c] = 0
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
            return
        
        for j in range(m):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[n-1][j] == 1:
                dfs(n-1, j)
        
        for i in range(n):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][m-1] == 1:
                dfs(i, m-1)
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res += 1
        return res