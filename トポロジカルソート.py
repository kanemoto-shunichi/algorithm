import sys
from collections import defaultdict, deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    H = int(input_data[0])
    W = int(input_data[1])

    grid = []
    idx = 2
    for _ in range(H):
        row = []
        for _ in range(W):
            row.append(input_data[idx])
            idx += 1
        grid.append(row)

    N = int(input_data[idx])
    idx += 1

    graph = defaultdict(list)
    nodes = set()

    for r in range(H):
        for c in range(W):
            nodes.add(grid[r][c])
    in_degree = {u: 0 for u in nodes}

    for _ in range (N):
        p = input_data[idx]
        v = input_data[idx + 1]
        idx += 2

        nodes.add(p)
        nodes.add(v)

        if p not in in_degree: in_degree[p] = 0
        if v not in in_degree: in_degree[v] = 0

        graph[p].append(v)
        in_degree[v] += 1
    
    queue = deque([u for u in nodes if in_degree[u] == 0])

    while queue:
        predator = queue.popleft()
        preys = set(graph[predator])

        if preys:
            to_remove = []
            for r in range(H):
                for c in range(W):
                    if grid[r][c] == predator:
                        for dr in [-1, 0, 1]:
                            for dc in [-1, 0, 1]:
                                if dr == 0 and dc == 0: continue
                                nr, nc = r + dr, c + dc
                                if 0 <= nr < H and 0 <= nc < W:
                                    if grid[nr][nc] in preys:
                                        to_remove.append((nr, nc))
                for r, c in to_remove:
                    grid[r][c] = '_'
            for v in graph[predator]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
    for row in grid:
        print(" ".join(row))

if __name__ == '__main__':
    solve()
