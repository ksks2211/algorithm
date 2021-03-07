n, m = map(int,input().split())
i,j,dir = map(int,input().split())

dirs = [(-1,0),(0,-1),(1,0),(0,1)]
field=[]

for _ in range(n):
    field.append(list(map(int,input().split())))

field[i][j]=2

tried, count = 0,1

while True:
    if tried == 4:
        next_i = i - dirs[dir][0]
        next_j = j - dirs[dir][1]

        # 뒤가 바다이면 종료 3-2
        if field[next_i][next_j]==1 :break

        # 바다가 아니면 방향은 유지 한칸뒤로 가서 처음부터 3-1
        i,j = next_i,next_j
        tried = 0
        #count += 1 # 중복 방문도 센다면?

    dir = (dir+1)%4
    next_i = i+dirs[dir][0]
    next_j = j+dirs[dir][1]

    # 다음 좌표로 이동 불가능 2-2
    if field[next_i][next_j]!=0 :
        tried+=1
        continue

    # 이동가능 2-1
    count += 1
    i,j = next_i, next_j
    field[i][j]=2
    tried = 0

print(count)