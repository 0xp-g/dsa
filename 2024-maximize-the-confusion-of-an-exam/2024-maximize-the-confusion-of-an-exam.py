class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        l = 0
        res = 0
        hmap = dict()
        hmap['T'] = 0
        hmap['F'] = 0
        for r in range(n):
            hmap[answerKey[r]] += 1

            while l <= r and r - l + 1 > max(hmap.values()) + k:
                hmap[answerKey[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res