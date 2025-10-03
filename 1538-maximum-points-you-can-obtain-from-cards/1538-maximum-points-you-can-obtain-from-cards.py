class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxsum = cursum = sum(cardPoints[:k])
        n = len(cardPoints)
        for i in range(1, k+1):
            cursum -= cardPoints[k-i]
            cursum += cardPoints[-i]
            maxsum = max(cursum, maxsum)
        return maxsum