import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        M = int(next(iterator))
        T = int(next(iterator))
        X = int(next(iterator))
    except StopIteration:
        return
    INF = 10**18
    dist = [[INF] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for _ in range(M):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        c = int(next(iterator))
        if c < dist[u][v]:
            dist[u][v] = dist[v][u] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    num_states = 1 << N
    dp = [[INF] * N for _ in range(num_states)]
    if X <= T:
        dp[1][0] = X
    else:
        print(0)
        return
    for mask in range(1, num_states):
        for u in range(N):
            if dp[mask][u] > T:
                continue
            for v in range(N):
                if (mask >> v) & 1:
                    continue
                new_time = dp[mask][u] + dist[u][v] + X
                if new_time <= T:
                    next_mask = mask | (1 << v)
                    if new_time < dp[next_mask][v]:
                        dp[next_mask][v] = new_time
    max_speeches = 0
    for mask in range(num_states):
        for u in range(N):
            if dp[mask][u] <= T:
                count = bin(mask).count('1')
                if count > max_speeches:
                    max_speeches = count
    print(max_speeches)

if __name__ == '__main__':
    solve()
    