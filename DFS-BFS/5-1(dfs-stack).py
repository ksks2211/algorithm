#Iterative - stack
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

    stack=[]
    visited[x][y]=1
    cases = [(1,0),(-1,0),(0,1),(0,-1)]

    while True:
        notExist = True
        for (i,j) in cases:
            a,b = x+i,y+j
            if valid_check(a,b) and visited[a][b] == 0: # have unvisited neighbor
                stack.append((x,y)) # current position to stack

                # move to unvisited neighbor
                visited[a][b]=1
                x,y = a,b
                notExist=False
                break

        if not stack : return  # end search
        # no unvisited neighbor. get back to earlier position.
        if notExist:
            (x,y) = stack.pop()

count = 0



for i in range(n):
    for j in range(m):
        if visited[i][j]==0 :
            count+=1
            bfs(i,j)


print(count)




