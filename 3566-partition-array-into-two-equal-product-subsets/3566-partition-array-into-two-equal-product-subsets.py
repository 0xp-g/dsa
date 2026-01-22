class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        total = prod(nums)
        if 0 in nums and target != 0: return False
        def solve(i, temp, runprod):
            if len(temp) != n and runprod == target and total // runprod == target:
                return True
            for j in range(i, n):
                temp.append(nums[i])
                if solve(j + 1, temp, runprod * nums[j]): return True
                temp.pop()
                if solve(j + 1, temp, runprod): return True
            return False
        res = solve(0, [], 1)
        print(res)
        return res