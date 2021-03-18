import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))

def validCheck(x,y):
    global  n, m
    if x>= n or x < 0 or y <0 or y >=m : return False
    return True

def bfs(graph,x,y):
    q = deque()
    q.append([x,y])

    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    graph[x][y] = -1
    while q:
        i, j = q.popleft()
        if (i==n-1 and j==m-1):return graph[i][j]*-1

        for dx,dy in dirs:
            tx,ty = i+dx, j+dy
            if validCheck(tx,ty) and graph[tx][ty]==1:
                graph[tx][ty]=graph[i][j]-1
                q.append([tx,ty])

    return -1


print(bfs(graph,0,0));