class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxsofar = nums[0]
        minsofar = nums[0]
        globalmax = nums[0]
        if len(nums) == 1:
            return nums[-1]
        for i, v in enumerate(nums):
            if i == 0:
                continue
            temp = minsofar
            tm = maxsofar
            minsofar = min(nums[i], nums[i]*temp, nums[i]*tm)
            maxsofar = max(nums[i], nums[i]*temp, nums[i]*tm) #max can become smaller when exploring deeper/ thus a global var that always stores the max state is required
            globalmax = max(globalmax, maxsofar)
        return globalmax