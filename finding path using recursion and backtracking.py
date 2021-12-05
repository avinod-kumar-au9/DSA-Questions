def isSafe(x, y, n, m):
    return x >=0 and x < n and y >=0 and y < m
 
def solve(x, y, n, m, grid, path, visited):
    if x < 0 or y < 0:
        return
 
    if x >= n or y >= m: # if i am outside my gride 
        return # it is an illegal state so i return
 
    if grid[x][y] == 1:
        return;
 
    if x == n - 1 and y == m - 1: # reached my target
        print(path)
        return
 
    if isSafe(x + 1, y, n, m) and visited[x+1][y] == False:
        visited[x+1][y] = True
        path.append('D')                                     
        solve(x + 1, y, n, m, grid, path, visited) 
        path.pop()
        visited[x+1][y] = False
 
    if isSafe(x, y + 1, n, m) and visited[x][y+1] == False:
        visited[x][y+1] = True
        path.append('R')
        solve(x, y + 1,n, m, grid, path, visited)
        path.pop()
        visited[x][y+1] = False
 
    if isSafe(x-1, y, n, m) and visited[x-1][y] == False:
        visited[x-1][y] = True
        path.append('U')
        solve(x - 1, y,n, m, grid, path, visited)
        path.pop()
        visited[x-1][y] = False
 
    if isSafe(x, y-1, n, m) and visited[x][y-1] == False:
        visited[x][y-1] = True
        path.append('L')
        solve(x, y - 1,n, m, grid, path, visited)
        path.pop()
        visited[x][y-1] = False
 
 
 
grid = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]
 
n = len(grid)
m = len(grid)
 
visited = [[False for _ in range(n)] for _ in range(m)]
print(visited)
visited[0][0] = True
 
solve(0, 0, n, m, grid, [], visited)