class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if len(matrix) == 1 and len(matrix[-1]) == 1:
            return True if matrix[0][0] == target else False
        row = len(matrix) - 1
        col = len(matrix[-1]) - 1

        c = col
        r = 0
        while r <= row and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False