class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        csum = sum(cardPoints[n-k:])
        maxsum = csum
        start = n-k
        end = 0
        while start < n:
            csum -= cardPoints[start]
            csum += cardPoints[end]
            maxsum = max(maxsum, csum)
            start += 1
            end += 1
        return maxsum