import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    M = int(input_data[0])
    N = int(input_data[1])

    grid = []
    idx = 2
    start_r, start_c = -1, -1

    for r in range(N):
        row = input_data[idx : idx + M]
        idx += M
        grid.append(row)
        if 's' in row:
            start_r = r
            start_c = row.index('s')
    
    queue = deque([(start_r, start_c, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[start_r][start_c] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c, dist = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc]:
                    cell = grid[nr][nc]
                    if cell == 'g':
                        print(dist + 1)
                        return
                    elif cell == '0':
                        visited[nr][nc] = True
                        queue.append((nr, nc, dist + 1))
    print("Fail")

if __name__ == "__main__":
    solve()