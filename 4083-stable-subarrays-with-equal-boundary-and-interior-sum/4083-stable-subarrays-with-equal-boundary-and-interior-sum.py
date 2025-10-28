class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        pfx = [0] * (n + 1)
        for i in range(n):
            pfx[i+1] = pfx[i] + capacity[i]
        res = 0
        hmap = defaultdict(int)
        hmap[(capacity[0], pfx[0+1])] = 1
        #(capacity[l], pfxsum[l+1])
        for r in range(2, n):
            target = pfx[r] - capacity[r]
            #target = pfx[l-1]
            res += hmap[(capacity[r], target)]
            l = r - 1 # ensuring r' - l + 1 >= 3 | r' > r
            hmap[(capacity[l], pfx[l+1])] += 1
        return res