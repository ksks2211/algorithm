n = int(input())
kList = list(map(int,input().split()))

d = [0]*(n+1)
d[1] = kList[0]
for i in range(2,n+1):
    d[i]=max(d[i-1],d[i-2]+kList[i-1])

print(d[n])
