class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = inf
        
        @cache
        def dp(i, j):
            if j < 0 or j >= m:
                return inf
            if i == n-1:
                return matrix[i][j]
            min_sum = min(dp(i+1, j-1), dp(i+1, j+1), dp(i+1, j))
            return matrix[i][j] + min_sum
        
        for j in range(m):
            res = min(res, dp(0, j))

        return res