class Solution:
    def longestPalindromeSubseq(self, s1: str) -> int:
        s2 = s1[::-1]
        n = len(s1)
        @lru_cache(None)
        def lcs(i, j):
            if i == n or j == n:
                return 0
            else:
                if s1[i] == s2[j]:
                    res = 1 + lcs(i+1, j+1)
                else:
                    res = max(lcs(i+1, j), lcs(i, j+1))
            return res
        return lcs(0, 0)