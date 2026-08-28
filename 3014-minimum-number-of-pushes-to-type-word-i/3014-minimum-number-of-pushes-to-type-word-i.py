class Solution:
    def minimumPushes(self, word: str) -> int:
        hmap = dict()
        cnt = 0
        val = 1
        res = 0

        for x in word:
            if cnt >= 8:
                cnt = 0
                val += 1 
            if x in hmap:
                res += hmap[x]
            else:
                hmap[x] = val
                res += val
            
            cnt += 1
        
        return res