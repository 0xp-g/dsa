class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def solve(i, res, curr, rem):
            if rem < 0:
                return 
            if rem == 0 and len(curr) == k:
                res.append(curr[:])
                return
            for j in range(i, 10):
                curr.append(j)
                solve(j+1, res, curr, rem-j)
                curr.pop()
            return
        solve(1, res, [], n)
        print(res)
        return res