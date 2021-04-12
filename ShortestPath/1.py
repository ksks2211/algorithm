import heapq
import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
INF = int(1e9)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    f, t = list(map(int, input().split()))
    graph[f].append(t)
    graph[t].append(f)

x, k = list(map(int, input().split()))


def dijkstra(start, end):
    global n, graph
    q = []
    dist = [INF] * (n + 1)
    dist[start] = 0

    heapq.heappush(q, (0,start))

    while q:
        c, i = heapq.heappop(q)
        if dist[i] < c: continue
        for j in graph[i]:
            cost = c + 1
            if cost < dist[j]:
                dist[j] = cost
                heapq.heappush(q, (cost,j))

    return dist[end]


res = dijkstra(1, k)
if (res != INF):
    res2 = dijkstra(k,x)
    if (res2 != INF):
        res+=res2
    else : res=-1
else: res=-1

print(res)

