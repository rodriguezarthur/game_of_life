def neighbors_number(grid, x, y):
    n = 0
    for i in range(x-1, x+2):
        for j in range(y-1,y+2):
            if i>=0 and i<len(grid[0]) and j>=0 and j<len(grid) and (i,j) != (x,y):
                if grid[j][i]:
                    n += 1
    return n

def enlarge_grid(grid):
    height = len(grid)
    width = len(grid[0])
    enlarged_grid = [[0 for i in range(width+2)] for i in range(height+2)]
    for i in range(height):
        for j in range(width):
            enlarged_grid[i+1][j+1] = grid[i][j]
    return enlarged_grid

def evolution(grid):
    height = len(grid)
    width = len(grid[0])
    new_grid = [[0 for i in range(width)] for i in range(height)]
    for i in range(height):
        for j in range(width):
            n = neighbors_number(grid,j,i)
            if grid[i][j]:
                if n==2 or n==3:
                    new_grid[i][j]=1
            else:
                if n==3:
                    new_grid[i][j]=1
        if (i==0 or i==height-1 or j==0 or j==width) and grid[i][j]:
            new_grid = enlarge_grid(new_grid)
    return new_grid