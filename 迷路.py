import sys
from collections import deque

def solve_step2(H, W, sy, sx, M, grid):
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    y, x = sy, sx
    for cmd in M:
        dy, dx = directions[cmd]
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != '#':
            y, x = ny, nx
    return y, x

def solve_step3(H, W, grid):
    sy, sx, gy, gx = -1, -1, -1, -1
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 'S':
                sy, sx = r, c
            elif grid[r][c] == 'G':
                gy, gx = r, c
    dist = [[-1] * W for _ in range(H)]
    dist[sy][sx] = 0
    queue = deque([(sy, sx)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        y, x = queue.popleft()
        if (y, x) == (gy, gx):
            return dist[y][x]
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != '#':
                if dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((ny, nx))
    return -1