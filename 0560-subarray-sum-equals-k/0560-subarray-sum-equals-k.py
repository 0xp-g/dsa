class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        hmap[0] += 1
        rsum, res = 0, 0
        for i in range(len(nums)):
            rsum += nums[i]
            if rsum - k in hmap:
                res += hmap[rsum-k]
            hmap[rsum] += 1
        return res