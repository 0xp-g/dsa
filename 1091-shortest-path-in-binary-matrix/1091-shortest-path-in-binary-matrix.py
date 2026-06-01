class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[-1])
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return -1
        if (n == 1 and m == 1) and grid[0][0] == 0:
            return 1
        dq = deque([(0, 0, 1)])
        visited = set()
        visited.add((0, 0))
        dirs = [(0, -1), (-1, 0),
                (0, 1), (1, 0), 
                (1, 1), (-1, -1),
                (1, -1), (-1, 1)
                ]
        while dq:
            for _ in range(len(dq)):
                r, c, dist = dq.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 1 and (nr, nc) not in visited:
                        if (nr, nc) == (n-1, m-1):
                            return dist+1
                        visited.add((nr, nc))
                        dq.append((nr, nc, dist + 1))
        return -1
