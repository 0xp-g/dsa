class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        def diag_sort(r, c):
            ogr, ogc = r, c
            temp = []
            while 0 <= r < m and 0 <= c < n:
                temp.append(mat[r][c])
                r += 1
                c += 1
            temp.sort()
            for x in temp:
                mat[ogr][ogc] = x
                ogr += 1
                ogc += 1
        
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    diag_sort(r, c)
        return mat