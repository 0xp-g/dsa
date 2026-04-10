class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        res = float('inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if i < j < k:
                        if nums[i] == nums[j] == nums[k]:
                            res = min(res, abs(i-j) + abs(j-k) + abs(k - i))
        return -1 if res == float('inf') else res