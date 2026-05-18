class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        piv = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                piv = i
                break
        
        
        if piv == -1:
            nums.reverse()
            return nums
        
        for idx in range(n-1, -1, -1):
            if nums[idx] > nums[piv]:
                nums[i], nums[idx]= nums[idx], nums[i]
                break
        
        nums[i+1:] = nums[i+1:][::-1]
        return nums