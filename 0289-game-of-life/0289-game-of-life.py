class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[-1])
        og = copy.deepcopy(board)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        for i in range(m):
            for j in range(n):
                live, dead = 0, 0
                for dx, dy in dirs:
                    nr = i + dx
                    nc = j + dy
                    if 0 <= nr < m and 0 <= nc < n:
                        if og[nr][nc] == 1:
                            live += 1
                        else:
                            dead += 1
                    else:
                        continue
                if og[i][j] == 1: #alive
                    if live < 2:
                        board[i][j] = 0
                    if live in [2, 3]:
                        continue
                    else:
                        board[i][j] = 0
                else:
                    if live == 3:
                        board[i][j] = 1
        return board
