class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9*num:
            return ''
        res = ''
        rsum = sum
        for _ in range(num):
            if rsum >= 9:
                res += '9'
                rsum -= 9
            elif 0 < rsum < 9:
                res += str(rsum)
                rsum -= rsum
            else:
                res += '0'
        return res