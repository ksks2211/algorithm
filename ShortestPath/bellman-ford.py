import sys

input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())

start = int(input())  # start node
graph = [[] for i in range(n + 1)]  # Adjacent List

predecessor = [0] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def bellmanford(s):
    global n, graph

    distance[s] = 0

    for _ in range(n - 1):
        for i in range(1, n + 1):
            for j, c in graph[i]:
                if distance[j] > distance[i] + c:
                    distance[j] = distance[i] + c
                    predecessor[j] = i

    for i in range(1, n + 1):
        for j, c in graph[i]:
            if distance[j] > distance[i] + c:
                distance[j] = -INF


bellmanford(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("Cant reach", end=" ")
    elif distance[i] == -INF:
        print("Negative Loop", end=" ")
    else:
        print(distance[i], end=" ")
