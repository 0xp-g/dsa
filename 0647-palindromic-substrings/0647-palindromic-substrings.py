class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        temp = 0
        for i in range(n):
            l, r = i - 1, i + 1
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                else:
                    temp += 1
                l -= 1
                r += 1
        for i in range(n-1):
            if s[i] == s[i+1]:
                temp += 1
                l, r = i - 1, i + 2
                while l >= 0 and r < n:
                    if s[l] != s[r]:
                        break
                    else:
                        temp += 1
                    l -= 1
                    r += 1
        return temp + n