class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums) #smallest number
        b = max(nums) #largest number

        #euclidean formula
        while(b!=0):
            temp = b
            b = a%b
            a = temp

        return a