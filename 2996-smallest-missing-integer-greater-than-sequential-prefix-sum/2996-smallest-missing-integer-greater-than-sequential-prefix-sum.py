class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        csum = nums[0]
        for j in range(1, n):
            if nums[j] == nums[j - 1] + 1:
                csum += nums[j]
            else:
                break
        nums = set(nums)
        curr = csum
        while True:
            if curr not in nums:
                return curr
            curr += 1