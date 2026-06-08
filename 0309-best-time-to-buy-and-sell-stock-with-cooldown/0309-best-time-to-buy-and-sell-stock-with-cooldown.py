class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n  = len(prices)
        @cache
        def dp(i, hold):
            if i >= n:
                return 0
            if hold:
                sell_now = prices[i] + dp(i+2, False)
                sell_later = dp(i+1, True)
                return max(sell_now, sell_later)
            else:
                buy_now = - prices[i] + dp(i+1, True) 
                buy_later = dp(i+1, False)
                return max(buy_now, buy_later)
        return dp(0, False)