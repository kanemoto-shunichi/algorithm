import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    H = int(input_data[0])
    W = int(input_data[1])
    grid = input_data[2:]
    lake_cells = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] == '#':
                lake_cells.append((r, c))
    total_lake = len(lake_cells)
    cant_build_count = 0
    for r, c in lake_cells:
        start_node = lake_cells[0]
        if start_node == (r, c):
            start_node = lake_cells[1]
        queue = deque([start_node])
        visited = set([start_node])
        while queue:
            curr_r, curr_c = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < H and 0 <= nc < W:
                    if grid[nr][nc] == '#' and (nr, nc) != (r, c) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        if len(visited) < total_lake -1:
            cant_build_count += 1
    ans = (H * W) - cant_build_count
    print(ans)

if __name__ == '__main__':
    solve()
    