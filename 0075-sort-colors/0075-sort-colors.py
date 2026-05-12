class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low = mid = 0
        high = n-1
        while low <= mid and mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1 #dont increment mid yet as it can have '0' which was swapped from high, we need to make sure it goes to low by the next iteration
            else:
                mid += 1
        return nums
