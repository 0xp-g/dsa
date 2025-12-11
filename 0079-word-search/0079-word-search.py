class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row = len(board)
        col = len(board[0])
        visited = set()
        
        def dfs(node, idx):
  
            i, j = node
            if i < 0 or j < 0 or i >= row or j >= col:
                return False
            
            if board[i][j] != word[idx]:
                return False

            if idx == len(word) - 1 and word[idx] == board[i][j]:
                return True

            elif word[idx] == board[i][j]:
                for x, y in [(i + 1, j), (i-1, j), (i, j + 1), (i, j - 1)]:
                    if (x, y) not in visited:
                        visited.add((x, y))
                        if dfs((x, y), idx + 1): return True
                        visited.remove((x, y))

            return False

        ref = word[0]
        
        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == ref:
                    visited.add((i, j))
                    if dfs((i, j), 0):
                        return True
                    visited.remove((i, j))

        return False