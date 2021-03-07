#Iterative
from collections import deque
n,m = map(int,input().split())

visited = []

for _ in range(n):
    visited.append(list(map(int, input())))

def valid_check(a,b):
    global n,m
    if a >=n or a<0 or b>=m or b<0 : return False
    return True

def bfs(x,y):
    global visited
    q = deque()
    q.append((x,y))

    while q:
        (a,b) = q.popleft()
        visited[a][b] = 1

        if valid_check(a+1,b) and visited[a+1][b]==0:q.append((a+1,b))
        if valid_check(a-1,b) and visited[a-1][b]==0:q.append((a-1,b))
        if valid_check(a,b+1) and visited[a][b+1]==0:q.append((a,b+1))
        if valid_check(a,b-1) and visited[a][b-1]==0:q.append((a,b-1))


count = 0

for i in range(n):
    for j in range(m):
        if visited[i][j]==0 :
            count+=1
            bfs(i,j)

print(count)




# for i in range(n):
#     for j in range(m):
#         print(visited[i][j],end=' ')
#     print()
