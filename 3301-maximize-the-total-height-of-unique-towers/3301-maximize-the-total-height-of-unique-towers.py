class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        maxval = maximumHeight[0]
        hmap = set()
        res = 0
        for i in range(len(maximumHeight)):
            temp = maximumHeight[i]
            if not hmap:
                minval = temp
                hmap.add(temp)
                res += temp
                continue
            while temp in hmap:
                temp = minval
                temp -= 1
            if temp <= 0:
                return -1
            minval = temp
            hmap.add(temp)
            res += temp
        return res