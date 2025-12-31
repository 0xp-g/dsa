class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[-1])
        if obstacleGrid[0][0] == 1:
            return 0
        @lru_cache(None)
        def dp(r, c):
            print(r, c)
            if r >= 0 and c >= 0 and obstacleGrid[r][c] == 1:
                return 0
            if r < 0 or c < 0:
                return 0
            if  (r == 0 and c == 0) and obstacleGrid[r][c] == 0:
                return 1
            if  (r == 0 or c == 0) and obstacleGrid[r][c] == 1:
                return 0
            return dp(r-1, c) + dp(r, c-1)
        return dp(m-1, n - 1)