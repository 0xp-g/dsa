class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @cache
        def dp(i, rem):
            if rem == 0:
                return 0
            
            if i >= n:
                return inf
            
            if rem < 0:
                return inf
            
            take = 1 + dp(i, rem-coins[i])
            not_take = dp(i+1, rem)

            return min(take, not_take)
        
        res = dp(0, amount)
        print(res)
        return res if res != inf else -1
