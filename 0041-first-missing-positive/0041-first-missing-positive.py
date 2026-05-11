class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hset = set()
        mex = 1
        for x in nums:
            hset.add(x)
            while mex in hset:
                mex += 1
        return mex