class Solution:
    def maximumTotalSum(self, ls: List[int]) -> int:
        ls.sort(reverse=True)
        ref = ls[0]-1
        for i in range(1, len(ls)):
            ls[i] = min(ls[i], ref)
            ref = ls[i]-1
            if ls[i] == 0:
                return -1
        print(ls)
        return sum(ls)