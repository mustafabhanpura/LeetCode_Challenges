class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)<=0 or grid is None:
            return 0
        
        r = len(grid)
        c = len(grid[0])
        
        for row in range(r):
            for col in range(c):
                
                if row == 0 and col == 0:
                    continue
                elif row-1<0:
                    grid[row][col] = grid[row][col] + grid[row][col-1]
                
                elif col-1<0:
                    grid[row][col] = grid[row][col] + grid[row-1][col]
                
                else:
                    grid[row][col] = grid[row][col] + min(grid[row-1][col],grid[row][col-1])
        
        return grid[r-1][c-1]