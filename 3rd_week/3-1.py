from collections import deque

import sys

# grid = [
#     [1, 1, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 1, 1, 1, 1]
# ]

# 11101
# 10101
# 10101
# 11111


grid = [list(map(int, line.strip())) for line in sys.stdin if line.strip()]

def bfs_maze(maze):
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    rows, cols = len(maze), len(maze[0])

    q = deque([(0, 0)])
    maze[0][0] = 1

    while q:
        x, y = q.popleft()

        if x == rows - 1 and y == cols - 1:
            return maze[x][y]

        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))

    return -1

print(bfs_maze(grid))




