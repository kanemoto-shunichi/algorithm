import sys
from collections import defaultdict, deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    M = int(input_data[1])
    adj = {i: [] for i in range(1, N + 1)}
    in_degree = {i: 0 for i in range(1, N + 1)}
    idx = 2

    for _ in range(M):
        h = int(input_data[idx])
        s = int(input_data[idx + 1])

        adj[h].append(s)
        in_degree[s] += 1
        idx += 2
    
    queue = deque([i for i in range(1, N + 1) if in_degree[i] == 0])
    result = []

    while queue:
        if len(queue) > 1:
            print("-1")
            return
        curr = queue.popleft()
        result.append(curr)

        for neighbor in adj[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(result) == N:
        print(" ".join(map(str, result)))
    else:
        print("-1")
if __name__ == '__main__':
    solve()
