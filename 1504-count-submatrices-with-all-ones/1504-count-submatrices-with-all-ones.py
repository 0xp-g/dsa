class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        h = [0] * m
        res = 0
        for i in range(n):
            for j in range(m):
                
                if mat[i][j] == 1:
                    h[j] += 1
                
                else:
                    h[j] = 0
                
                minh = inf
                for k in range(j, -1, -1):
                    minh = min(h[k], minh)
                    if minh == 0:
                        break
                    
                    res += minh

        return res