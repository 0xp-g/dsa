# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 0
        hi = n
        while lo <= hi:
            ver = (lo + hi)// 2
            if isBadVersion(ver):
                res = ver
                hi = ver - 1
            else:
                lo = ver + 1
        return res