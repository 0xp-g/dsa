''' 
Q1. Check if Any Element Has Prime Frequency
Solved
Easy
3 pt.
You are given an integer array nums.

Return true if the frequency of any element of the array is prime, otherwise, return false.

The frequency of an element x is the number of times it occurs in the array.

A prime number is a natural number greater than 1 with only two factors, 1 and itself.

 

Example 1:

Input: nums = [1,2,3,4,5,4]

Output: true

Explanation:

4 has a frequency of two, which is a prime number.

Example 2:

Input: nums = [1,2,3,4,5]

Output: false

Explanation:

All elements have a frequency of one.

Example 3:

Input: nums = [2,2,2,4,4]

Output: true

Explanation:

Both 2 and 4 have a prime frequency.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

'''
from collections import Counter
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        x = Counter(nums)
        for num in x.values():
            if num < 2:
                continue
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                return True
        return False
                