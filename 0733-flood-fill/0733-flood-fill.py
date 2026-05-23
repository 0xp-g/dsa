class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = grid[sr][sc]
        print(color)
        n = len(grid)
        m = len(grid[0])

        def dfs(r, c):
            print(r, c)
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == newColor or grid[r][c] != color:
                return
            
            grid[r][c] = newColor
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
            return
        
        dfs(sr, sc)
        
        return grid