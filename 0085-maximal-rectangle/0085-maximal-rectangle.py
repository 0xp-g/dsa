class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        m = len(matrix)
        n = len(matrix[-1])
        arr = [0 for _ in range(n)]
        area = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    arr[j] += 1
                else:
                    arr[j] = 0
                
            area = max(area, self.area(arr))
        return area

    def area(self, arr):

        n = len(arr)
        pse = [-1] * n
        nse = [n] * n
        st1 = []
        st2 = []

        for i in range(n):
            while st1 and arr[i] <= arr[st1[-1]]:
                st1.pop()
            if st1:
                pse[i] = st1[-1]
            st1.append(i)
        
        for i in range(n-1, -1, -1):
            while st2 and arr[i] <= arr[st2[-1]]:
                st2.pop()
            if st2:
                nse[i] = st2[-1]
            st2.append(i)
            
        area = 0

        for i in range(n):
            w = nse[i] - pse[i] - 1
            area = max(area, arr[i] * w)
        
        return area