class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        hmap = SortedDict()
        n = len(limit)
        res = 0

        for i in range(n):
            if limit[i] not in hmap:
                hmap[limit[i]] = []
                hmap[limit[i]].append(value[i])
            else:
                hmap[limit[i]].append(value[i])

        for k in hmap.keys():
            hmap[k] = sorted(hmap[k], reverse=True)

        for k in hmap.keys():
            #limit
            if len(hmap[k]) <= k:
                res += sum(hmap[k])
            else:
                res += sum(hmap[k][:k])
        
        print(hmap)
        return res