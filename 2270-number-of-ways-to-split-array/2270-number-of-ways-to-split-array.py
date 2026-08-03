class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        pfx= [0] * (n+1)

        for i in range(n):
            pfx[i+1] = pfx[i] + nums[i]
        
        res = 0
        for i in range(n):
            if i == n-1:
                break
            
            if pfx[i+1] >= (pfx[n] - pfx[i+1]):
                res += 1
        return res