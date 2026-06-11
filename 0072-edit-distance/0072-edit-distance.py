class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        @cache
        def dp(i, j):
            if i == n1:
                return n2-j
            if j == n2:
                return n1-i
            if word1[i] == word2[j]:
                return dp(i+1, j+1)
            else:
                return 1 + min(dp(i+1, j), dp(i, j+1), dp(i+1, j+1))
        
        return dp(0, 0)