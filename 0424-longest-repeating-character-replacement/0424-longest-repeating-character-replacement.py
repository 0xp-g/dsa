class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        res = 1
        hmap = dict()
        for r in range(n):
            hmap[s[r]] = hmap.get(s[r], 0) + 1
            while l <= r and (r-l+1) - max(hmap.values()) > k:
                hmap[s[l]] -= 1
                if hmap[s[l]] == 0:
                    del hmap[s[l]]
                l += 1
            res = max(res, r-l+1)
        return res