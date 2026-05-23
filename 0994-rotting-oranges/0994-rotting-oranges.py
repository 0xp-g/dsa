class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        n, m = len(grid), len(grid[0])
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    dq.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        while dq:
            r, c, t = dq.popleft()

            for dr, dc in [(0, -1), (1, 0), (-1, 0), (0, 1)]:
                nr = r+dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    fresh -= 1
                    grid[nr][nc] = 2
                    dq.append((nr, nc, t+1))
                
            if fresh == 0:
                return t+1
        
        return -1