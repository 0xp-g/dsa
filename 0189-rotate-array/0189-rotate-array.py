class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if n == 0 or k == 0:
            return
        temp = nums[n-k:]
        for i in range(n-k-1, -1, -1):
            nums[i+k] = nums[i]
        nums[:k] = temp