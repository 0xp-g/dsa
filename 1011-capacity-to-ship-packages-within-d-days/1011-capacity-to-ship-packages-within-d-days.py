class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lsum, l, n = sum(weights), min(weights), len(weights)
        r = lsum
        
        def helper(mid):
            i = 0
            for _ in range(days):
                running = 0
                while running < mid:
                    if running + weights[i] > mid:
                        break
                    else:
                        running += weights[i]
                        i += 1
                        if i == n:
                            return True
            return False

        res = 1
        while l <= r:
            mid = (l + r) // 2
            if helper(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res