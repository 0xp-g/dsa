class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        hmap = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}

        curr = ''

        res = []

        self.helper(digits, 0, hmap, curr, res)

        return res

    def helper(self, digits, idx, hmap, curr, res):

        if len(curr) == len(digits):

            res.append(curr)

            return 

        for i in range(idx, len(digits)):

            for x in hmap[int(digits[i])]:

                self.helper(digits, idx + 1, hmap, curr + x, res)
                
            break