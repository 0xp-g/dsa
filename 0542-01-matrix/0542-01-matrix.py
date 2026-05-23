class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        dq = deque()

        n = len(grid)
        m = len(grid[-1])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dq.append((i, j, 0))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1
        
        while dq:

            r, c, d = dq.popleft()
            for dr, dc in [(0,-1),(1,0),(-1,0),(0,1)]:


                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == -1:
                    grid[nr][nc] = d + 1
                    dq.append((nr, nc, d+1))
        
        return grid