class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        rowIndex += 1
        for i in range(1, rowIndex):
            res.append(res[i-1] * (rowIndex-i) // (i))
        return res