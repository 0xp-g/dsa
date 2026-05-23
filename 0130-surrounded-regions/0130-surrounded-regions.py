class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m, visited = len(grid), len(grid[-1]), set()
        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 'X' or grid[r][c] =='S':
                return
            
            visited.add((r, c))
            grid[r][c] = 'S'
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
            return
        
        for c in range(m):
            if grid[0][c] == 'O':
                dfs(0, c)
            if grid[n-1][c] == 'O':
                dfs(n-1, c)
        
        for r in range(n):
            if grid[r][0] == 'O':
                dfs(r, 0)
            if grid[r][m-1] == 'O':
                dfs(r, m-1)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'S':
                    grid[i][j] = 'O'
                elif grid[i][j] == 'O':
                    grid[i][j] = 'X'

        return 