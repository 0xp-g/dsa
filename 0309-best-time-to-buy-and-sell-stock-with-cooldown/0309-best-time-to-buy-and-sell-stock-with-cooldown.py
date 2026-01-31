class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(i, state):
            if i >= n:
                return 0
            if state == 0:
                buy = -prices[i] + dp(i + 1, 1)
                notbuy = dp(i + 1, state)
                res = max(buy, notbuy)
            else:
                sell = prices[i] + dp(i+2, 0)
                notsell = dp(i+1, state)
                res = max(sell, notsell)
            return res
        return dp(0, 0)