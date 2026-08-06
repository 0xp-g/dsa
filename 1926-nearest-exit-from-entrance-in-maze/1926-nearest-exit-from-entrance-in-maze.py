class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        #border cells goal
        #entrance is not exit
        n, m = len(maze), len(maze[-1])
        dq = deque()
        dq.append((entrance[0], entrance[1], 0))
        dirs = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        vis = set()
        vis.add((entrance[0], entrance[1]))
        while dq:
            for _ in range(len(dq)):
                x, y, cost = dq.popleft()
                for dr, dc in dirs:
                    nr, nc = x + dr, y + dc
                    if 0<=nr<n and 0 <= nc < m and maze[nr][nc] == '.' and (nr, nc) not in vis:
                        if nr == 0 or nr == n-1 or nc == 0 or nc == m-1 and [nr, nc] != entrance:
                            return cost + 1
                        dq.append((nr, nc, cost + 1))
                        vis.add((nr, nc))
        return -1    