def minPathSum(grid):
        
        M, N = len(grid), len(grid[0])
        
        for i in range(M):
            grid[i][0] = grid[i][0] + grid[i-1][0] if i > 0 else grid[i][0]
            for j in range(1,N):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j] if i > 0 else grid[i][j-1]+grid[i][j]
        return grid[-1][-1]



print(minPathSum( [[1,7,1],[1,5,1],[4,2,1]]))
