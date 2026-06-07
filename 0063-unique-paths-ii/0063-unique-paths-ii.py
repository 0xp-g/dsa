class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[-1])
        if obstacleGrid[0][0] == 1:
            return 0
        @cache
        def dp(i, j):
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            return dp(i-1, j) + dp(i, j-1)
        return dp(n-1, m-1)