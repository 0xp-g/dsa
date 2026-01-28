class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @lru_cache(None)
        def dp(i, holding):

            if i >= len(prices):
                return 0
            
            if holding:
                sell = prices[i] + dp(i + 1, False)
                wait = dp(i + 1, True)
                result = max(sell, wait)
            else:
                buy = -prices[i] + dp(i + 1, True)
                wait = dp(i + 1, False)
                result = max(buy, wait)
            
            return result

        return dp(0, False)