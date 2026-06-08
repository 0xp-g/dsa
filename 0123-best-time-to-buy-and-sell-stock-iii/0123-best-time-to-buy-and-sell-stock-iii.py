class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n  = len(prices)
        @cache
        def dp(i, hold, k):
            if i == n or k == 2:
                return 0
            if hold:
                sell_now = prices[i] + dp(i, False, k+1)
                sell_later = dp(i+1, True, k)
                return max(sell_now, sell_later)
            else:
                buy_now = - prices[i] + dp(i+1, True, k) 
                buy_later = dp(i+1, False, k)
                return max(buy_now, buy_later)
        return dp(0, False, 0)