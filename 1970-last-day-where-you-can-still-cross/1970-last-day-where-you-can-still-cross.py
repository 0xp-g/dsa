class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def solve(mid):

            grid2 = [[0 for _ in range(col)] for _ in range(row)]
            for i in range(mid):
                x, y = cells[i]
                grid2[x-1][y-1] = 1

            pq = deque()
            for r in [0]:
                for c in range(col):
                    if grid2[r][c] == 0:
                        pq.append((r, c))
            while pq:
                cr, cc = pq.popleft()
                if cr == row - 1:
                    return True
                else:
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr = cr + dr
                        nc = cc + dc
                        if 0 <= nr <= row - 1 and 0 <= nc <= col - 1 and grid2[nr][nc] == 0:
                            pq.append((nr, nc))
                            grid2[nr][nc] = 1

            return False

        l = 1; r = len(cells)
        plb = None
        while l <= r:

            mid = (l + r) // 2
            if solve(mid):

                plb = mid
                l = mid + 1
            else:
                r = mid - 1

        return plb #BFS + BS