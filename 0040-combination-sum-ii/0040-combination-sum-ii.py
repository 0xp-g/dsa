class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res, n = [], len(nums)
        nums.sort()
        def backtrack(i, cel, csum):
            if csum == target:
                res.append(cel[:])
                return
            if i >= n or csum > target:
                return
            cel.append(nums[i])
            backtrack(i+1, cel, csum+nums[i])
            cel.pop()
            for idx in range(i, n):
                if nums[idx] != nums[i]:
                    backtrack(idx, cel, csum)
                    break
            return 
        backtrack(0, [], 0)
        return res