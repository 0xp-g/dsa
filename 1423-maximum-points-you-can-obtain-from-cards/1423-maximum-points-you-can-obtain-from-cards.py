class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints) - 1
        l = 0
        r = k - 1
        temp = sum(cardPoints[:k])
        res = temp
        for _ in range(k):
            temp = temp - cardPoints[r] + cardPoints[n]
            res = max(res, temp)
            n -= 1
            r -= 1
        return res
