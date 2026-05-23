class Solution:
    def check(self, nums: List[int]) -> bool:
        dip = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                print(nums[i], nums[i+1])
                dip += 1

        if nums[0] < nums[-1]:
            dip += 1
        print(dip)
        return dip <= 1