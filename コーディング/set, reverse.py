import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    H = int(input_data[0])
    grid = [list(row) for now in input_data[1:H+1]]
    while True:
        to_erase = set()
        for r in range(H):
            for c in range(5):
                if grid[r][c] == '.':
                    continue
                val = grid[r][c]
                neighbors = []
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < H and 0 <= nc < 5:
                        neighbors.append((nr, nc))
                all_same = True
                for nr, nc in neighbors:
                    if grid[nr][nc] != val:
                        all_same = False
                        break
                if all_same:
                    to_erase.add((r, c))
                    for nr, nc in neighbors:
                        to_erase.add((nr, nc))
        if not to_erase:
            break
        for r, c in to_erase:
            grid[r][c] = '.'
        for c in range(5):
            new_col = []
            for r in range(H - 1, -1, -1):
                if grid[r][c] != '.':
                    new_col.append(grid[r][c])
            while len(new_col) < H:
                new_col.append('.')
            new_col.reverse()
            for r in range(H):
                grid[r][c] = new_col[r]
    for row in grid:
        print("".join(row))

if __name__ == '__main__':
    solve()

