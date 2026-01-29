class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(i, hold, cap):
            if i >= n or cap == 0:
                return 0
            
            if hold:
                #we can sell it today or sell it tomorrow:
                sell = prices[i] + dp(i + 1, False, cap-1)
                wait = dp(i + 1, True, cap)
                res = max(sell, wait)
            else:
                #not holding stock, means we can buy today or wait and buy tomorrow
                buy = -prices[i] + dp(i + 1, True, cap)
                wait = dp(i + 1, False, cap)
                res = max(buy, wait)

            return res
        return dp(0, False, k)
