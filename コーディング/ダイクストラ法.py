import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    X = int(input_data[1])
    F = int(input_data[2])
    S = int(input_data[3])
    dist = [[-1] * (X + 1) for _ in range(N + 1)]
    pq = [(0, 0, X)]
    dist[0][X] = 0
    while pq:
        t, l, s = heapq.heappop(pq)
        if l == N:
            print(t)
            return
        if dist[l][s] != -1 and dist[l][s] < t:
            continue
        nl = l + s
        if nl > N:
            nl = N
        ns = s - F
        if ns < 0:
            ns = 0
        if dist[nl][ns] == -1 or dist[nl][ns] > t + 1:
            dist[nl][ns] = t + 1
            heapq.heappush(pq, (t + 1, nl, ns))
        nl_sleep = l
        ns_sleep = s + S
        if ns_sleep > X:
            ns_sleep = X
        if dist[nl_sleep][ns_sleep] == -1 or dist[nl_sleep][ns_sleep] > t + 3:
            dist[nl_sleep][ns_sleep] = t + 3
            heapq.heappush(pq, (t + 3, nl_sleep, ns_sleep))

if __name__ == '__main__':
    solve()


    