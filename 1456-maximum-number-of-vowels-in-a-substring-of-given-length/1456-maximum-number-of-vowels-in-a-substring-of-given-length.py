class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        globalvar = 0
        n = len(s)
        res = 0
        temp = Counter(s[0:k])
        for v in vowels:
            if v in temp:
                res += temp[v]
        globalvar = max(globalvar, res)
        for i in range(k, n):
            temp[s[i-k]] -= 1
            if not temp[s[i-k]]:
                del temp[s[i-k]]
            temp[s[i]] = temp.get(s[i], 0) + 1
            res = 0
            for v in vowels:
                if v in temp:
                    res += temp[v]
            globalvar = max(globalvar, res)
        return globalvar
            