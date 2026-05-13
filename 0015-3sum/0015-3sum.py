class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n-1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum < 0:
                    l += 1
                    continue
                elif current_sum > 0:
                    r -= 1
                    continue
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res