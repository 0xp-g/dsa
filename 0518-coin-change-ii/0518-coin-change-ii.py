class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def dp(i, rem):
            if rem == 0:
                return 1
            
            if i >= n:
                return 0
            
            if rem < 0:
                return 0
            
            take =  dp(i, rem-coins[i])
            not_take = dp(i+1, rem)

            return take + not_take
        
        res = dp(0, amount)
        return res 
