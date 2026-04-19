class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        grid = [[0] * m for _ in range(n)]
        q = deque()

        # initialize
        for r, c, color in sources:
            grid[r][c] = color
            q.append((r, c, color))

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            size = len(q)
            next_cells = {}  

            for _ in range(size):
                r, c, color = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                        if (nr, nc) not in next_cells:
                            next_cells[(nr, nc)] = color
                        else:
                            next_cells[(nr, nc)] = max(next_cells[(nr, nc)], color)

            for (r, c), color in next_cells.items():
                grid[r][c] = color
                q.append((r, c, color))

        return grid