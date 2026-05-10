class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n, res = len(nums), []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                l, r = j+1, n-1
                while l < r:
                    if l > j+1 and nums[l] == nums[l-1]:
                        l += 1
                        continue
                    csum = nums[i] + nums[j] + nums[l] + nums[r]
                    if csum < target:
                        l += 1
                    elif csum > target:
                        r -= 1
                    else:
                        res.append((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
        return res