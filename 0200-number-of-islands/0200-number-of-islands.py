class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or ((r, c) in visited) or grid[r][c] == '0':
                return

            visited.add((r, c))
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
            #dfs(r-1, c-1)
            #dfs(r+1, c+1)
            #dfs(r-1, c+1)
            #dfs(r+1, c-1)
            return
        
        res = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    res += 1
                    dfs(i, j)
                    
        return res

