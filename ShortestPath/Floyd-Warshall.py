import sys
INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m= int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    graph[a][a]=0

for _ in range(m):
    a,b,c= map(int,input().split())
    graph[a][b]=c


for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j : continue
        for k in range(1,n+1):
            if k==j: continue
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])


for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INF",end=" ")
        else:
            print(graph[a][b],end=" ")

    print()