class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(nums, k):
            hmap = {'odd' : 0}
            res = 0
            l = 0
            for r in range(len(nums)):
                if nums[r] % 2 == 1:
                    hmap['odd'] += 1
                while hmap['odd'] > k:
                    if nums[l] % 2 == 1:
                        hmap['odd'] -= 1
                    l += 1
                res += r - l + 1
            return res   
        return atMost(nums, k) - atMost(nums, k-1)     