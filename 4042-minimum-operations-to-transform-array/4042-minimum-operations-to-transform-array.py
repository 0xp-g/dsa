class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        x = nums2[n1]
        flag = False
        res = 0
        appCost = float('inf')
        for i in range(n1):
            res += abs(nums1[i] - nums2[i])
            if not flag:
                if min(nums1[i], nums2[i]) <= x <= max(nums1[i], nums2[i]):
                    appCost = 1
                    flag = True
                elif not flag:
                    appCost = min(appCost, 1 + abs(x - nums1[i]), 1 + abs(x - nums2[i]))
        return res + appCost