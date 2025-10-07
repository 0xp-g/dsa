class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        candidates.sort()
        self.solve(candidates, target, 0, 0, curr, res)
        return res
    def solve(self, candidates, target, idx, csum, curr, res):
        if idx > len(candidates):
            return 
        if csum > target:
            return 
        if csum == target:
            res.append(curr[:])
            return 
        for i in range(idx, len(candidates)):
            if csum + candidates[i] > target:
                break
            csum += candidates[i]
            curr.append(candidates[i])
            self.solve(candidates, target, i, csum, curr, res)
            csum -= candidates[i]
            curr.pop()