import sys

sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        A_strs = []
        for _ in range(N):
            A_strs.append(next(iterator))
    except StopIteration:
        return
    MOD = 10**9 + 7
    A = []
    L = []
    for s in A_strs:
        val = int(s)
        length = len(s)
        A.append(val)
        L.append(length)
    max_len_sum = sum(L)
    fact = [1] * (N + 1)
    for i in range(2, N + 1):
        fact[i] = (fact[i-1] * i) % MOD
    pow10 = [1] * (max_len_sum + 1)
    for i in range(1, max_len_sum + 1):
        pow10[i] = (pow10[i-1] * 10) % MOD
    dp = [[0] * (max_len_sum + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    curr_max_s = 0
    for length in L:
        for k in range(N, 0, -1):
            for s in range(curr_max_s + length, length - 1, -1):
                if dp[k-1][s-length] > 0:
                    dp[k][s] = (dp[k][s] + dp[k-1][s-length]) % MOD
        curr_max_s += length
    total_sum = 0
    for i in range(N):
        val = A[i]
        length = L[i]
        temp_dp = [row[:] for row in dp]
        for k in range(1, N + 1):
            for s in range(length, max_len_sum + 1):
                temp_dp[k][s] = (temp_dp[k][s] - temp_dp[k-1][s-length]) % MOD
        coef = 0
        for k in range(N):
            perm_count = (fact[k] * fact[N - 1 - k]) % MOD
            for s in range(max_len_sum - length + 1):
                if temp_dp[k][s] != 0:
                    ways = (temp_dp[k][s] * perm_count) % MOD
                    term = (ways * pow10[s]) % MOD
                    coef = (coef + term) % MOD
        term_total = (val * coef) % MOD
        total_sum = (total_sum + term_total) % MOD
    print(total_sum)

if __name__ == '__main__':
    solve()   