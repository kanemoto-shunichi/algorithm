import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    X = int(input_data[1])
    R = int(input_data[2])
    menus = []
    idx = 3
    for _ in range(N):
        t_i = int(input_data[idx])
        s_i = int(input_data[idx + 1])
        menus.append((t_i, s_i))
        idx += 2
    dp = [-1] * (X + 1)
    dp[X] = 0
    for t_i, s_i in menus:
        next_dp = [-1] * (X + 1)
        for j in range(X + 1):
            if dp[j] != -1:
                rest_stamina = min(X, j + R)
                if dp[j] > next_dp[rest_stamina]:
                    next_dp[rest_stamina] = dp[j]
                if j >= s_i:
                    train_stamina = j - s_i
                    if dp[j] + t_i > next_dp[train_stamina]:
                        next_dp[train_stamina] = dp[j] + t_i
        dp = next_dp
    print(max(dp))
if __name__ == '__main__':
    solve()