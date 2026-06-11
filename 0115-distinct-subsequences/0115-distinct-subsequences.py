class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1, n2 = len(s), len(t)

        @cache
        def dp(i, j):
            if j == n2:
                return 1
            
            if i >= n1:
                return 0
            
            take = 0
            if s[i] == t[j]:
                take = dp(i+1, j+1)
            not_take = dp(i+1, j)

            return take+not_take
        
        return dp(0, 0)