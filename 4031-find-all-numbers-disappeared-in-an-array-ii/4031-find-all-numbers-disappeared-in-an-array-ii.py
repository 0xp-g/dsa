class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        bound_set = set(nums)
        res = []
        curr = []

        for i in range(lower, upper + 1):
            if not curr and i not in bound_set:
                curr = [i, i]

            if i in bound_set:
                if curr:
                    res.append(curr)
                curr = []

            else:
                curr[1] = max(curr[1], i)
                if i == upper:
                    if curr:
                        res.append(curr)

        return res