class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        gph = [set() for _ in range(n)]
        for x, y in trust:
            gph[x-1].add(y - 1)
        candidates = []
        for i in range(n):
            if gph[i] == set():
                candidates.append(i)
        cd = None
        for c in candidates:
            for i in range(n):
                if c != i and c not in gph[i]:
                    cd = None
                    break
                cd = c
        if cd == 0: return 1
        return cd + 1 if cd else -1