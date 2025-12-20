class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hset = set()
        l = 0
        hmap = dict()
        maxlen = 1
        hmap[fruits[l]] = 1
        for r in range(1, len(fruits)):
            hmap[fruits[r]] = hmap.get(fruits[r], 0) + 1
            while l < r and len(hmap) > 2:
                lf = fruits[l]
                hmap[lf] -= 1
                if not hmap[lf]:
                    del hmap[lf]
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen