class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)

        is_pal_memo = [[-1] * n for _ in range(n)]
        def is_pal(left, right):
            if is_pal_memo[left][right] != -1:
                return is_pal_memo[left][right]
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            is_pal_memo[left][right] = is_pal(left + 1, right - 1)
            return is_pal_memo[left][right]

        memo = [float('inf')] * n

        def dp(i):
            if memo[i] != float('inf'):
                return memo[i]
            if is_pal(i, n-1):
                return 0
            cuts = float('inf')
            for j in range(i, n):
                if is_pal(i, j):
                    cuts = min(cuts, 1 + dp(j+1))
            memo[i] = cuts
            return cuts
        return dp(0)