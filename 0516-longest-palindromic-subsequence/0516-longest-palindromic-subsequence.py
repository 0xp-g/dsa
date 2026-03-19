class Solution:
    def longestPalindromeSubseq(self, s1: str) -> int:
        s2 = s1[::-1]
        n = len(s1)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == n or j == n:
                    continue
                else:
                    if s1[i] == s2[j]:
                        dp[i][j] = 1 + dp[i+1][j+1]
                    else:
                        dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]