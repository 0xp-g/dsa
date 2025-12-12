class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        pfx = [0] * (n + 1)
        res = 0
        for i in range(n): pfx[i+1] = pfx[i] + damage[i]   
        for j in range(n):
            t = requirement[j] - hp + pfx[j+1]
            i = bisect_left(pfx, t, 0, j+1)
            res += j - i + 1
        return res 