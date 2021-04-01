import sys

n,m = list(map(int,sys.stdin.readline().rstrip().split()))
d=[m+1]*(10001)
moneys=[]

for _ in range(n):
    money = int(sys.stdin.readline().rstrip())
    d[money]=1
    moneys.append(money)

d[0]=0
moneys.sort()
smallest =moneys[0]

for i in range(smallest+1,m+1):
    for money in moneys:
        if i-money>=0:
            tmp=d[i-money]
            if tmp!=(m+1): d[i]=min(d[i],tmp+1)
        else : break

if d[m]!=m+1 : print(d[m])
else : print(-1)
