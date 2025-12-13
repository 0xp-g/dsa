class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dp(n):

            if n == 0:
                return 0
            if n < 0:
                return float('inf')
            mincost = float('inf')
            for c in coins:
                res = dp(n-c)
                if res == float('inf') or res == -1: continue
                mincost = min(mincost, res + 1)
            return mincost if mincost != float('inf') else -1

        return dp(amount)