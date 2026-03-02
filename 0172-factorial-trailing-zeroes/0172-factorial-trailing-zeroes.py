class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        ref = 5
        res = 0
        while True:
            if n//ref >= 1:
                res += n//ref
                ref *= 5
            else:
                break
        return res