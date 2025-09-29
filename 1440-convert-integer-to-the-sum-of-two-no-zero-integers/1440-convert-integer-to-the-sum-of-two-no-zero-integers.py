class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        l, r = 1, n-1
        while l <= r:
            if '0' not in str(l) and '0' not in str(r):
                return [l, r] 
            l += 1; r -= 1

