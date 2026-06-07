class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        @cache
        def dp(i, j):
            if i == 0 or j == 0:
                return 1
            return dp(i-1, j) + dp(i, j-1)
        return dp(n-1, m-1)