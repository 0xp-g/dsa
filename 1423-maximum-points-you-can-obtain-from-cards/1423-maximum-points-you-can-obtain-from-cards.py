class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        rsum = sum(cardPoints[n-k:])
        l = n-k
        r = n-1
        maxsum = rsum
        while l < n:
            rsum -= cardPoints[l]
            l += 1
            r = (r+1) % n
            rsum += cardPoints[r]
            maxsum = max(maxsum, rsum)
        return maxsum