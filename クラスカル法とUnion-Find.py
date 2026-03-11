import sys

sys.setrecursionlimit(20000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    edges = []
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        edges.append((c, u, v))
        idx += 3
    edges.sort(key=lambda x: x[0])
    parent = list(range(N+1))

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]
    
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_j] = root_i
            return True
        return False
    
    components = N
    max_cost = 0

    for c, u, v in edges:
        if union(u, v):
            max_cost = c
            components -= 1
            if components == 1:
                break
    print(max_cost + 1)

if __name__ == '__main__':
    solve()