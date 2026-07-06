class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        for i in intervals:
            i.append(abs(i[1]-i[0]))
        intervals.sort(key = lambda x:(x[0], -x[2]))
        res = []
        for a, b, _ in intervals:
            if not res:
                res.append([a, b])
            else:
                if res[-1][0] <= a and res[-1][1] >= b:
                    continue
                else:
                    res.append([a, b])
        return len(res)