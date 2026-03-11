import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        H = int(next(iterator))
        W = int(next(iterator))
        N = int(next(iterator))
    except StopIteration:
        return
    total_score = 0
    for _ in range(N):
        grid = []
        start_pos = None
        goal_pos = None
        for r in range(H):
            row_vals = []
            for c in range(W):
                val_str = next(iterator)
                if val_str == 'S':
                    start_pos = (r, c)
                    row_vals.append(0)
                elif val_str == 'G':
                    goal_pos = (r, c)
                    row_vals.append(0)
                else:
                    row_vals.append(int(val_str))
            grid.append(row_vals)
        dist = [[-1] * W for _ in range(H)]
        max_coins = [[-1] * W for _ in range(H)]
        sr, sc = start_pos
        gr, gc = goal_pos
        dist[sr][sc] = 0
        max_coins[sr][sc] = 0
        queue = deque([(sr, sc)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()
            curr_dist = dist[r][c]
            curr_coin = max_coins[r][c]
            if dist[gr][gc] != -1 and curr_dist >= dist[gr][gc]:
                continue
            for dr, dc in directions:
                nr, nc = r + dr, c +dc
                if 0 <= nr < H and 0 <= nc < W:
                    next_cost = grid[nr][nc]
                    if dist[nr][nc] == -1:
                        dist[nr][nc] = curr_dist + 1
                        max_coins[nr][nc] = curr_coin + next_cost
                        queue.append((nr, nc))
                    elif dist[nr][nc] == curr_dist + 1:
                        if curr_coin + next_cost > max_coins[nr][nc]:
                            max_coins[nr][nc] = curr_coin + next_cost
        total_score += max_coins[gr][gc]
    print(total_score)

if __name__ == '__main__':
    solve()

