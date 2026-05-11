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
            cel.append(nums[i]) #nums[i] picked here
            backtrack(i+1, cel, csum+nums[i])
            cel.pop()
            for idx in range(i, n): #im setting up to ignore all the nums[i] so that in the next depth i pick something that is not equal to nums[i] (bcos if we pick nums[i] in the next depth, it is guaranteed that we will have a duplicate combination as we already picked nums[i] above.)
                if nums[idx] != nums[i]:
                    backtrack(idx, cel, csum)
                    break
            return 
        backtrack(0, [], 0)
        return res