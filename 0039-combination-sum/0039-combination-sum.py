class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        def backtrack(i, curr, rsum):
            if rsum == 0:
                res.append(curr[:])
                return

            if rsum < 0 or i == n:
                return 
            
            curr.append(nums[i])
            backtrack(i, curr, rsum-nums[i])
            curr.pop()
            backtrack(i+1, curr, rsum)
            return res
        
        res = []
        backtrack(0, [], target)
        return res