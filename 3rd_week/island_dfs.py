def island_dfs_stack(grid):
    # 방향 배열: 오른쪽, 왼쪽, 아래, 위
    direction_x = [0, 0, 1, -1]
    direction_y = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    island_count = 0

    for row_idx in range(rows):
        for col_idx in range(cols):
            if grid[row_idx][col_idx] != '1':
                continue

            island_count += 1
            stack = [(row_idx, col_idx)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'
                for i in range(4):
                    next_x = x + direction_x[i]
                    next_y = y + direction_y[i]
                    if next_x < 0 or next_x >= rows or next_y < 0 or next_y >= cols or grid[next_x][next_y] != '1':
                        continue
                    stack.append((next_x, next_y))
    return island_count

assert island_dfs_stack(grid=[
    ["0", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3

def island_dfs_recursive(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    m = len(grid)
    n = len(grid[0])
    cnt = 0

    def dfs_recursive(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return

        # 방문처리
        grid[r][c] = '0'
        for i in range(4):
            dfs_recursive(r + dx[i], c + dy[i])
        return

    for r in range(m):
        for c in range(n):
            node = grid[r][c]
            if node != '1':
                continue

            cnt += 1
            dfs_recursive(r, c)

    return cnt

assert island_dfs_recursive(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3