from collections import deque

def timeToRot(grid):
    m = len(grid)
    n = len(grid[0])
    rotten = deque()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                rotten.append((i, j))

    if len(rotten) == 0:
        return -1

    prevCount = len(rotten)
    currCount = 0
    transformed = False
    rotTime = 0

    while rotten:
        x, y = rotten.popleft()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for dx, dy in directions:
            if 0 <= x + dx < m and 0 <= y + dy < n:
                if grid[x + dx][y + dy] == 1:
                    grid[x + dx][y + dy] = 2
                    transformed = True
                    rotten.append((x + dx, y + dy))
                    currCount += 1
            else:
                continue
        prevCount -= 1
        if prevCount == 0 and transformed:
            rotTime += 1
            transformed = False
            prevCount = currCount
            currCount = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return -1
    
    return rotTime if rotTime > 0 else -1

# grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
grid = [[2, 2, 2], [0, 2, 2], [2, 0, 2]]
res = timeToRot(grid)
print(res)

    
