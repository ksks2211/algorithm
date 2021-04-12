import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n + 1)]

for i in range(1,n+1):
    graph[i][i]=0

for _ in range(m):
    f, t = list(map(int, input().split()))
    graph[f][t]=graph[t][f]=1

x, k = list(map(int, input().split()))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j : continue
        for k in range(j+1,n+1):
            if k==i : continue
            graph[j][k] = graph[k][j] = min(graph[j][k],graph[j][i]+graph[i][k])

res1 = graph[1][k]
res2 = graph[k][x]

if(res1 ==INF or res2==INF):
    print(-1)
else :
    print(res1+res2)





