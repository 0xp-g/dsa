class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hmap = {}
        for x in s:
            if x in hmap:
                return x
            hmap[x] = True