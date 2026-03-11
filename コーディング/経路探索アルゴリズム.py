import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    M = int(input_data[1])
    A = []
    idx = 2
    for _ in range(N):
        row = []
        for _ in range(M):
            row.append(int(input_data[idx]))
            idx += 1
        A.append(row)
    X = int(input_data[idx])
    idx += 1
    curr_s = 0
    total_fare = 0
    for _ in range(X):
        r = int(input_data[idx]) - 1
        s = int(input_data[idx + 1]) - 1
        idx += 2
        fare = abs(A[r][s] - A[r][curr_s])
        total_fare += fare
        curr_s = s
    print(total_fare)

if __name__ == '__main__':
    solve()


