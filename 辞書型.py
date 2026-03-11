import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return
    dict = {k : 1 for k in range(1, N + 1)}
    for _ in range(M):
        x = int(next(iterator))
        y = int(next(iterator))
        dict[x] += dict[y]
        dict[y] = 0
    max_len = max(dict.values())
    for k in range(1, N + 1):
        if dict[k] == max_len:
            print(k)
if __name__ == '__main__':
    solve()