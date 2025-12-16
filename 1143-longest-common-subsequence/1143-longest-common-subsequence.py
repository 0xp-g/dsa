class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        l1 = len(s1)
        l2 = len(s2)
        res = 0
        @cache
        def recurse(i, j):
            if i == l1 or j == l2:
                return 0
            if s1[i] == s2[j]:
                return 1 + recurse(i + 1, j + 1)
            else:
                return max(recurse(i + 1, j),recurse(i, j + 1))
        res = recurse(0, 0)
        return res