class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        
        def palindrome(s):
            return s == s[::-1]

        def backtrack(i, cset):
            if i == n:
                res.append(cset[:])
            
            for idx in range(i, n):
                if palindrome(s[i:idx+1]):
                    cset.append(s[i:idx+1])
                    backtrack(idx+1, cset)
                    cset.pop()

        backtrack(0, [])
        return res