class Solution:
    def maxSubarrayLength(self, arr: List[int], k: int) -> int:
        n = len(arr)
        l = 0
        hmap = dict()
        res = 1
        for r in range(n):
            hmap[arr[r]] = hmap.get(arr[r], 0) + 1
            while hmap[arr[r]] > k:
                hmap[arr[l]] -= 1
                if hmap[arr[l]] == 0:
                    del hmap[arr[l]]
                l += 1
            res = max(res, r - l + 1)
        return res