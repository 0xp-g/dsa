class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        hset = set()
        ls = []
        answer = 0

        def conflict(nr, nc, ls) -> bool:
            nonlocal res
            for r, c in ls:
                if r == nr or c== nc or abs(r-nr) == abs(c-nc):
                    return True
            return False
            
        def solve(r, c, ls):
            nonlocal answer
            if r == n-1:
                answer += 1
                res.append(ls[:])
                return
            for nr in range(1):
                for nc in range(0, n):
                    nr = r + 1
                    if conflict(nr, nc, ls):
                        if nc == n-1:
                            return False
                        continue
                    else:
                        ls.append([nr, nc])
                        solve(nr, nc, ls)
                        ls.pop()            
        solve(-1, -1, [])
        return answer

        ans = []
        for valid in res:
            board = [['.'] * n for _ in range(n)]
            for x, y in valid:
                board[x][y] = "Q"
            temp = []
            for row in board:
                s= ''.join(row)
                temp.append(s)
            ans.append(temp)
        return ans