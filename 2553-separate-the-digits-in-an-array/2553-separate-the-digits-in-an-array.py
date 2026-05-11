class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ls = []
        for x in nums:
            if x >= 10:
                for y in str(x):
                    ls.append(int(y))
            else:
                ls.append(x)
        return ls