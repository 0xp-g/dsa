class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hmap = dict()
        maxval = 0
        for right in range(len(s)):
            hmap[s[right]] = hmap.get(s[right], 0) + 1
            while (right - left + 1) - max(hmap.values()) > k:
                hmap[s[left]] = hmap.get(s[left], 0) - 1
                if not hmap[s[left]]:
                    del hmap[s[left]]
                left += 1
            maxval = max(maxval, right - left + 1)
        return maxval


