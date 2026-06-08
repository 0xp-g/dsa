class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n  = len(prices)
        @cache
        def dp(i, hold, transactions_so_far):
            if i == n or transactions_so_far == k:
                return 0
            if hold:
                sell_now = prices[i] + dp(i, False, transactions_so_far+1)
                sell_later = dp(i+1, True, transactions_so_far)
                return max(sell_now, sell_later)
            else:
                buy_now = - prices[i] + dp(i+1, True, transactions_so_far) 
                buy_later = dp(i+1, False, transactions_so_far)
                return max(buy_now, buy_later)
        return dp(0, False, 0)