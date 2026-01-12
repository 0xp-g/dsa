class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[inf for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1 if dungeon[m-1][n-1] > 0 else abs(dungeon[m-1][n-1]) + 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                elif j == n-1:
                    hp = dp[i+1][j]
                elif i == m-1:
                    hp = dp[i][j + 1]
                else:
                    hp = min(dp[i + 1][j], dp[i][j + 1])
                # need - (gain/loss) = hp
                need = hp - dungeon[i][j]
                dp[i][j] = 1 if need <= 0 else need
        return dp[0][0]