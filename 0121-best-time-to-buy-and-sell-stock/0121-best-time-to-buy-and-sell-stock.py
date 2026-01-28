class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, holding):

            if i >= len(prices):
                return 0
            
            if holding:
                do_sell = prices[i] 
                do_wait = dp(i + 1, True)
                result = max(do_sell, do_wait)
            else:
                do_buy = -prices[i] + dp(i + 1, True)
                do_wait = dp(i + 1, False)
                result = max(do_buy, do_wait)
            
            return result

        return dp(0, False)