class Solution {

    public void solveSudoku(char[][] board) {
        solve(board);
    }

    public boolean solve(char[][] board) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                if (board[row][col] == '.') {
                    for (char val = '1'; val <= '9'; val++) {

                        if (!isViolation(board, row, col, val)) {
                            board[row][col] = val;
                            if (solve(board)) {
                                return true;
                            }
                            board[row][col] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    public boolean isViolation(char[][] board, int row, int col, char val) {
        for (int i = 0; i < 9; i++) {

            if (board[row][i] == val) {
                return true;
            }
            if (board[i][col] == val) {
                return true;
            }
        }
        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;
        for (int r = startRow; r < startRow + 3; r++) {
            for (int c = startCol; c < startCol + 3; c++) {
                if (board[r][c] == val) {
                    return true;
                }
            }
        }
        return false;
    }
}