#recursive

n,m = map(int,input().split())

visited = []

for _ in range(n):
    visited.append(list(map(int, input())))

def valid_check(a,b):
    global n,m
    if a >=n or a<0 or b>=m or b<0 : return False
    return True

def bfs(x,y):
    visited[x][y]=1
    cases = [(1,0),(-1,0),(0,1),(0,-1)]

    for (i,j) in cases:
        a,b = x+i,y+j
        if valid_check(a,b) and visited[a][b]==0: bfs(a,b)

count = 0

for i in range(n):
    for j in range(m):
        if visited[i][j]==0 :
            count+=1
            bfs(i,j)

print(count)

