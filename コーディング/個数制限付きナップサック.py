import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        V = int(next(iterator))
    except StopIteration:
        return
    dp = [0] * (V + 1)

    for _ in range(N):
        x = int(next(iterator))
        v = int(next(iterator))
        c = int(next(iterator))

        if c * v >= V:
            for j in range(v, V + 1):
                if dp[j - v] + x > dp[j]:
                    dp[j] = dp[j - v] + x
        else:
            k = 1
            while c > 0:
                take = min(k, c)
                w_take = v * take
                x_take = x * take
                for j in range(V, w_take - 1, -1):
                    if dp[j - w_take] + x_take > dp[j]:
                        dp[j] = dp[j - w_take] + x_take
                c -= take
                k *= 2
    print(dp[V])

if __name__ == '__main__':
    solve()

