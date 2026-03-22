class Solution:
    def isMatch(self, text: str, pat: str) -> bool:
        n1 = len(text)
        n2 = len(pat)
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[n1][n2] = True
        for j in range(n2):
            flag= False
            for idx in range(j, n2):
                if pat[idx] != '*':
                    flag = True
                    break
            if not flag:
                dp[n1][j] = True
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if text[i] == pat[j] or pat[j] == '?':
                    dp[i][j] = dp[i+1][j+1]
                elif pat[j] == '*':
                    dp[i][j] = dp[i][j+1] or dp[i+1][j]
        return dp[0][0]