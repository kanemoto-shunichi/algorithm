import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        H = int(next(iterator))
        W = int(next(iterator))
    except StopIteration:
        return
    dp = [int(next(iterator)) for _ in range(W)]
    for _ in range(1, H):
        next_dp = [0] * W
        row = [int(next(iterator)) for _ in range(W)]
        if W == 1:
            next_dp[0] = dp[0] + row[0]
        else:
            next_dp[0] = row[0] + max(dp[0], dp[1])
            for j in range(1, W-1):
                next_dp[j] = row[j] + max(dp[j - 1], dp[j], dp[j + 1])
            next_dp[W - 1] = row[W - 1] + max(dp[W - 2], dp[W - 1])
        dp = next_dp
    print(max(dp))

if __name__ == '__main__':
    solve()
