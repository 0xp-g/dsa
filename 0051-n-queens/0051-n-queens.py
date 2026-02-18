class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        '''board = [['.'] * n] * n
        res = []
        hset = set()
        ls = []
        def conflict(nr, nc, ls) -> bool:
            nonlocal res
            for r, c in ls:
                if r == nr or c== nc or abs(r-nr) == abs(c-nc):
                    return True
            return False

        def solve(r, c, ls) :
            if r == n-1:
                res.append(ls[:])
                return

            for nr in range(r+1, n):
                for nc in range(0, n):
                    if conflict(nr, nc, ls):
                        if nc == n-1:
                            return False
                        continue
                    else:
                        ls.append([nr, nc])
                        #if not solve(nr, nc, ls): 
                        #    return
                        ls.pop()
        solve(-1, -1, [])
        for x in res:
            print(x)'''

        res = []
        hset = set()
        ls = []
        def conflict(nr, nc, ls) -> bool:
            nonlocal res
            for r, c in ls:
                if r == nr or c== nc or abs(r-nr) == abs(c-nc):
                    return True
            return False

        def solve(r, c, ls):
            if r == n-1 and len(ls) == n:
                res.append(ls[:])
                return

            for nr in range(r+1, n):
                for nc in range(0, n):
                    if conflict(nr, nc, ls):
                        if nc == n-1:
                            return False
                        continue
                    else:
                        ls.append([nr, nc])
                        solve(nr, nc, ls)
                        ls.pop()            
        solve(-1, -1, [])

        for x in res:
            print(x)

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