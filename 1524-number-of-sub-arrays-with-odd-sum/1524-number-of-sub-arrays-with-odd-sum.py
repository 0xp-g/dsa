class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd_pfx = [0] 
        even_pfx = [1]
        pfx = 0
        MOD = 10 ** 9 + 7
        
        for x in arr:
            pfx += x
            if pfx % 2 == 1:
                odd_pfx.append(odd_pfx[-1] + 1) 
                even_pfx.append(even_pfx[-1])
            else:
                odd_pfx.append(odd_pfx[-1]) 
                even_pfx.append(even_pfx[-1] + 1)

        pfx = 0
        res = 0
        
        for i, x in enumerate(arr):
            pfx += x
            if pfx % 2 == 0:
                res += odd_pfx[i]
            else:
                res += even_pfx[i]
                
        return res % MOD