class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @lru_cache(None)
        def dp(i, target):
            if target == 0:
                return 0
            if i >= n or target < 0:
                return float('inf')
            take = 1 + dp(i, target - coins[i])
            nottake = 0 + dp(i + 1, target)
            res = min(take, nottake)
            return res
        res =  dp(0, amount)
        return res if res != float('inf') else -1