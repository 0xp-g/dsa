class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        graph = [[' '] * cols for _ in range(rows)]
        print(cols)
        t = 0
        for i in range(rows):
            for j in range(cols):
                graph[i][j] = encodedText[t]
                t += 1
        res = []
        i, j = 0, 0
        start_j = 0
        while start_j != cols:
            res.append(graph[i][j])
            i += 1
            j += 1
            if i == rows or j == cols:
                start_j += 1
                j = start_j
                i = 0
        return ''.join(res).rstrip()