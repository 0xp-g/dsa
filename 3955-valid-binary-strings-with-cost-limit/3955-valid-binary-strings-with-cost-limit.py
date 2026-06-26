class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        res = []
        def backtrack(ls, cost):
            if len(ls) == n:
                if cost <= k:
                    res.append(''.join(ls[:]))
                return
            
            if cost > k:
                return
            
            if ls and ls[-1] == '1':
                backtrack(ls + ['0'], cost)
                return
            backtrack(ls + ['1'], cost + len(ls))
            backtrack(ls + ['0'], cost)
            return
        

        backtrack([], 0)
        return res