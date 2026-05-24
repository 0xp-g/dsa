class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = float('-inf')
        curr = 0
        for x in nums:
            if x == 1:
                curr += 1
            else:
                res = max(res, curr)
                curr = 0
        res = max(res, curr)
        return res