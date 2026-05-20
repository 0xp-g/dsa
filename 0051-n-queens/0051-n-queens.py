class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def violation_xists(i, j, rowmap, colmap, coords):
            if i in rowmap:
                return True
            elif j in colmap:
                return True
            for r, c in coords: 
                if abs(r-i) == abs(c-j):
                    return True
            return False
        
        def backtrack(r, rowmap, colmap, coords):
            if r == n:
                board = [['.'] * n for _ in range(n)]
                for i, j in coords:
                    board[i][j] = 'Q'
                for i in range(n):
                    board[i] = ''.join(board[i])
                res.append(board[:])
                return True

            for i in range(n):
                if not violation_xists(r, i, rowmap, colmap, coords):
                    rowmap.add(r)
                    colmap.add(i)
                    coords.append((r, i))
                    backtrack(r+1, rowmap, colmap, coords)
                    rowmap.discard(r)
                    colmap.discard(i)
                    coords.pop()
        backtrack(0, set(), set(), [])
        return res