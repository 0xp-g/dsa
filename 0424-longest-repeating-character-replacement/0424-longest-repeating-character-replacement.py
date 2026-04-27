class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        maxlen, l = 1, 0
        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r], 0) + 1
            while l <= r and (r-l+1) - max(hmap.values()) > k:
                hmap[s[l]] -= 1
                if not hmap[s[l]]:
                    del hmap[s[l]]
                l += 1
            maxlen = max(maxlen, r-l+1)
        return maxlen